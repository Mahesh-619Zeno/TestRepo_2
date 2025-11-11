<?php
declare(strict_types=1);
session_start([
    'cookie_httponly' => true,
    'cookie_secure'   => isset($_SERVER['HTTPS']),
    'use_strict_mode' => true,
    'cookie_samesite' => 'Strict'
]);

// --- Security Headers ---
header('X-Frame-Options: DENY');
header('X-XSS-Protection: 1; mode=block');
header('X-Content-Type-Options: nosniff');

// --- Include database configuration ---
require "../config.php";

// --- Helper Functions ---

// Generate CSRF token
function generate_csrf_token(): string {
    $_SESSION['csrf_token'] = bin2hex(random_bytes(32));
    return $_SESSION['csrf_token'];
}

// Verify CSRF token
function verify_csrf_token(string $token): bool {
    if (empty($_SESSION['csrf_token']) || !hash_equals($_SESSION['csrf_token'], $token)) {
        return false;
    }
    unset($_SESSION['csrf_token']); // prevent reuse
    return true;
}

// Unified JSON response
function json_response(bool $success, string $title, string $message, ?string $redirect = null): never {
    header('Content-Type: application/json; charset=utf-8');
    echo json_encode(compact('success', 'title', 'message', 'redirect'), JSON_UNESCAPED_UNICODE);
    exit;
}

// --- Redirect if already logged in ---
if (!empty($_SESSION['loggedin']) && $_SESSION['loggedin'] === true) {
    $role = $_SESSION['user']['role'] ?? 'user';
    $location = ($role === 'admin') ? '../admin/' : '../';
    header("Location: $location");
    exit;
}

// --- Generate CSRF token for the form ---
$csrf_token = generate_csrf_token();

// --- Handle POST Request ---
if ($_SERVER['REQUEST_METHOD'] === 'POST') {

    // Reject non-AJAX requests (optional but good)
    $is_ajax = isset($_SERVER['HTTP_X_REQUESTED_WITH']) && strtolower($_SERVER['HTTP_X_REQUESTED_WITH']) === 'xmlhttprequest';
    if (!$is_ajax) {
        header('HTTP/1.1 403 Forbidden');
        exit('Direct POST requests not allowed.');
    }

    // 1. Validate CSRF token
    if (!verify_csrf_token($_POST['csrf_token'] ?? '')) {
        json_response(false, '❌ Xato!', 'Xavfsizlik tokeni (CSRF) xatosi.');
    }

    // 2. Sanitize and validate input
    $username = strtolower(trim($_POST['username'] ?? ''));
    $password = $_POST['password'] ?? '';

    if ($username === '' || $password === '') {
        json_response(false, '⚠️ Diqqat!', 'Iltimos, login va parol maydonlarini to‘ldiring!');
    }

    try {
        $db = new Database();

        // 3. Fetch user data securely
        $user_data = $db->select('users', 'id, name, username, password, role', 'username = ?', [$username], 's');

        // Unified error for user-not-found or password mismatch
        if (empty($user_data) || !password_verify($password, $user_data[0]['password'])) {
            json_response(false, '❌ Xato!', 'Login yoki parol noto‘g‘ri.');
        }

        $user = $user_data[0];

        // 4. Successful login — regenerate session
        session_regenerate_id(true);
        $_SESSION['loggedin'] = true;
        $_SESSION['user'] = [
            'id' => (int)$user['id'],
            'name' => $user['name'],
            'username' => $user['username'],
            'role' => $user['role'],
        ];

        $redirect_url = ($user['role'] === 'admin') ? '../admin/' : '../';

        json_response(true, '✅ Muvaffaqiyat!', 'Tizimga kirdingiz!', $redirect_url);

    } catch (Throwable $e) {
        error_log("Login error: " . $e->getMessage());
        json_response(false, '❌ Xato!', 'Tizimda xatolik yuz berdi. Iltimos, keyinroq urinib ko‘ring.');
    }
}
?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Login Page</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" />
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" />
    <script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>
    <style>
        .card {
            border-radius: 1rem;
            border: none;
        }

        .v-100 {
            min-height: 100vh;
        }
    </style>
</head>

<body class="bg-light">
    <div class="container">
        <div class="row justify-content-center align-items-center v-100">
            <div class="col-md-6 col-lg-4">
                <div class="card shadow">
                    <div class="card-body p-4">
                        <h2 class="text-center mb-4">Login</h2>
                        <form id="loginForm" method="POST" autocomplete="off">
                            <!-- CSRF Token -->
                            <input type="hidden" name="csrf_token" value="<?= htmlspecialchars($csrf_token) ?>">

                            <div class="mb-3">
                                <label for="username" class="form-label">Username</label>
                                <input type="text" class="form-control" name="username" id="username"
                                    placeholder="Enter username" required autocomplete="username" />
                            </div>

                            <div class="mb-3 position-relative">
                                <label for="password" class="form-label">Password</label>
                                <div class="input-group">
                                    <input type="password" id="password" class="form-control" name="password"
                                        placeholder="Enter password" required autocomplete="current-password" />
                                    <button class="btn btn-outline-secondary" type="button"
                                        onclick="togglePassword('password')" aria-label="Show/Hide Password">
                                        <i class="fas fa-eye"></i>
                                    </button>
                                </div>
                            </div>

                            <button type="submit" class="btn btn-primary w-100">Login</button>
                        </form>
                        <p class="text-center mt-3">Don't have an account? <a href="../signup/">Sign Up</a></p>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>

    <script>
        function togglePassword(id) {
            const input = document.getElementById(id);
            const icon = input.parentElement.querySelector('i');
            input.type = input.type === 'password' ? 'text' : 'password';
            icon.classList.toggle('fa-eye');
            icon.classList.toggle('fa-eye-slash');
        }

        document.getElementById('loginForm').addEventListener('submit', async function (e) {
            e.preventDefault();

            const form = this;
            const submitButton = form.querySelector('button[type="submit"]');

            if (!form.username.value || !form.password.value) {
                Swal.fire({
                    icon: 'warning',
                    title: '⚠️ Diqqat!',
                    text: 'Iltimos, login va parol maydonlarini to‘ldiring!'
                });
                return;
            }

            submitButton.disabled = true;

            try {
                const formData = new FormData(form);

                const response = await fetch('', {
                    method: 'POST',
                    headers: { 'X-Requested-With': 'XMLHttpRequest' },
                    body: formData
                });

                if (!response.ok) throw new Error('Server error');

                const result = await response.json();

                if (result.success) {
                    await Swal.fire({
                        icon: 'success',
                        title: result.title,
                        text: result.message,
                        showConfirmButton: false,
                        timer: 1500
                    });
                    if (result.redirect) window.location.href = result.redirect;
                } else {
                    Swal.fire({ icon: 'error', title: result.title, text: result.message });
                }
            } catch (err) {
                console.error(err);
                Swal.fire({
                    icon: 'error',
                    title: '❌ Tarmoq xatosi',
                    text: 'Server bilan bog‘lanishda muammo yuz berdi.'
                });
            } finally {
                submitButton.disabled = false;
            }
        });
    </script>
</body>

</html>

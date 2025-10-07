<?php
if (session_status() === PHP_SESSION_NONE) {
    session_start();
}


// --- Configuration & Initialization ---

// Function to generate and retrieve CSRF token
function get_csrf_token() {
    if (empty($_SESSION['csrf_token'])) {
        $_SESSION['csrf_token'] = bin2hex(random_bytes(32));
    }
    return $_SESSION['csrf_token'];
}
$csrf_token = htmlspecialchars(get_csrf_token(), ENT_QUOTES, 'UTF-8');

// Function to handle JSON response output
function json_response($success, $title, $message, $redirect = null) {
    header('Content-Type: application/json');
    echo json_encode([
        'success' => $success,
        'title' => $title,
        'message' => $message,
        'redirect' => $redirect
    ]);
    exit;
}

// Redirect if already logged in
if (isset($_SESSION['loggedin']) && $_SESSION['loggedin'] === true) {
    $role = $_SESSION['user']['role'];
    $location = ($role === 'admin') ? '../admin/' : '../';
    header("Location: $location");
    exit;
}

// Include database configuration (assuming it contains the Database class)
include "../config.php";
// $db = new Database(); // Assuming Database class is available

// --- POST Request Handling ---

if ($_SERVER['REQUEST_METHOD'] === "POST") {
    
    // 1. CSRF Token Validation
    if (!isset($_POST['csrf_token']) || $_POST['csrf_token'] !== $_SESSION['csrf_token']) {
        json_response(false, '❌ Xato!', 'Xavfsizlik tokeni (CSRF) xatosi.', null);
    }
    
    // Invalidate the token immediately after successful check to prevent reuse
    unset($_SESSION['csrf_token']);
    
    // 2. Input Sanitization and Retrieval
    $username = strtolower(trim($_POST['username'] ?? ''));
    $password = $_POST['password'] ?? '';

    // 3. Basic Input Validation
    if (empty($username) || empty($password)) {
        json_response(false, '⚠️ Diqqat!', "Iltimos, login va parol maydonlarini to‘ldiring!", null);
    }

    // 4. Database Interaction
    try {
        // NOTE: $db instantiation depends on config.php contents
        $db = new Database(); 
        $user_data = $db->select('users', '*', 'username = ?', [$username], 's');
        
        if (empty($user_data)) {
            json_response(false, '❌ Foydalanuvchi topilmadi!', "Bunday foydalanuvchi topilmadi.");
        }
        
        $user = $user_data[0];
        $hashedPassword = $user['password'];

        if (password_verify($password, $hashedPassword)) {
            // 5. Successful Login
            $_SESSION['loggedin'] = true;
            $_SESSION['user'] = [
                'id' => $user['id'],
                'name' => $user['name'],
                'username' => $user['username'],
                'role' => $user['role'],
            ];

            $redirect_url = ($user['role'] === 'admin') ? '../admin/' : '../';
            
            // 6. Security Header (optional, but good practice)
            session_regenerate_id(true);

            json_response(true, '✅ Muvaffaqiyat!', 'Tizimga kirdingiz!', $redirect_url);
        } else {
            // 7. Password Mismatch
            json_response(false, '❌ Xato parol!', 'Noto‘g‘ri parol, qayta urinib ko‘ring.');
        }

    } catch (Exception $e) {
        // 8. Database Error Handling
        error_log("Database error during login: " . $e->getMessage());
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
        .v-100 { min-height: 100vh; }
    </style>
</head>

<body class="bg-light">
    <div class="container">
        <div class="row justify-content-center align-items-center v-100">
            <div class="col-md-6 col-lg-4">
                <div class="card shadow">
                    <div class="card-body p-4">
                        <h2 class="text-center mb-4">Login</h2>
                        <form id="loginForm" method="POST">
                            <!-- CSRF Token -->
                            <input type="hidden" name="csrf_token" value="<?= htmlspecialchars($csrf_token, ENT_QUOTES, 'UTF-8') ?>">

                            <div class="mb-3">
                                <label for="username" class="form-label">Username</label>
                                <input type="text" class="form-control" name="username" id="username"
                                    placeholder="Enter username" required />
                            </div>
                            <div class="mb-3 position-relative">
                                <label for="password" class="form-label">Password</label>
                                <div class="input-group">
                                    <input type="password" id="password" class="form-control" name="password"
                                        placeholder="Enter password" required />
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
        function togglePassword(fieldId) {
            const input = document.getElementById(fieldId);
            const button = input.nextElementSibling.querySelector('button'); // Adjusted selector
            const icon = button.querySelector('i');

            if (input.type === 'password') {
                input.type = 'text';
                icon.classList.replace('fa-eye', 'fa-eye-slash');
            } else {
                input.type = 'password';
                icon.classList.replace('fa-eye-slash', 'fa-eye');
            }
        }

        document.getElementById('loginForm').addEventListener('submit', async function (e) {
            e.preventDefault();

            const form = this;
            const submitButton = form.querySelector('button[type="submit"]');
            
            // Basic Client-side check
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
                    headers: {
                        'X-Requested-With': 'XMLHttpRequest'
                    },
                    body: formData
                });

                if (!response.ok) {
                    throw new Error('Server returned an unexpected status.');
                }

                const result = await response.json();

                if (result.success) {
                    await Swal.fire({
                        icon: 'success',
                        title: result.title,
                        text: result.message,
                        confirmButtonText: 'OK',
                        showConfirmButton: false,
                        timer: 1500
                    });
                    if (result.redirect) {
                        window.location.href = result.redirect;
                    }
                } else {
                    Swal.fire({
                        icon: 'error',
                        title: result.title,
                        text: result.message
                    });
                }
            } catch (error) {
                Swal.fire({
                    icon: 'error',
                    title: '❌ Tarmoq xatosi',
                    text: 'Server bilan bog‘lanishda muammo yuz berdi.'
                });
                console.error('Fetch error:', error);
            } finally {
                submitButton.disabled = false;
            }
        });
    </script>
</body>

</html>

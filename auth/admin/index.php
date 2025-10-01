<?php
session_start();

// --- Access Control & Initialization ---

// Check 1: Ensure user is logged in
if (!isset($_SESSION['loggedin']) || $_SESSION['loggedin'] !== true) {
    header('Location: ../login/');
    exit;
}

$user = $_SESSION['user'] ?? null;

// Check 2: Ensure user data is valid and role is 'admin'
if (empty($user) || !isset($user['role']) || $user['role'] !== 'admin') {
    // If logged in but not admin, redirect to the main site (assuming this is the standard user path)
    header('Location: ../'); 
    exit;
}

// Extract user details for display, providing safe fallbacks
$userName = htmlspecialchars($user['name'] ?? $user['username'] ?? 'Administrator');
$userRole = htmlspecialchars(ucfirst($user['role'] ?? 'Unknown'));

// --- Security Headers ---
header('X-Frame-Options: DENY');
header('X-Content-Type-Options: nosniff');
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin Dashboard - Welcome</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" />
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
            <div class="col-md-8 col-lg-6">
                <div class="card shadow-lg">
                    <div class="card-body p-5">
                        <div class="text-center mb-5">
                            <!-- Admin icon from Font Awesome -->
                            <i class="fas fa-crown fa-3x text-primary mb-3"></i> 
                            <h1 class="card-title fw-bold text-success">Admin Access Granted</h1>
                            <p class="text-muted">Welcome to the secure administrative area.</p>
                        </div>
                        
                        <!-- Personalized Welcome -->
                        <h2 class="h3 mb-3">Hello, <?= $userName ?>!</h2>
                        
                        <div class="alert alert-info d-flex align-items-center" role="alert">
                            <i class="fas fa-user-shield me-3"></i>
                            <div>
                                Your current role: <strong><?= $userRole ?></strong>
                            </div>
                        </div>

                        <p class="card-text mt-4">
                            You currently have **elevated privileges** to manage system settings, user accounts, and content moderation.
                            Please proceed with caution.
                        </p>

                        <hr>

                        <div class="d-grid gap-2 mt-4">
                            <a href="../admin/dashboard.php" class="btn btn-success btn-lg">
                                <i class="fas fa-tachometer-alt me-2"></i> Go to Dashboard
                            </a>
                            <a href="../logout/" class="btn btn-outline-secondary">
                                <i class="fas fa-sign-out-alt me-2"></i> Secure Logout
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
</body>

</html>

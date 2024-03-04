<?php
// Check if the form was submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Get form data
    $name = $_POST["name"];
    $email = $_POST["email"];
    $message = $_POST["message"];

    // Validate form data (optional)
    if (empty($name) || empty($email) || empty($message)) {
        echo "Please fill in all fields";
        exit;
    }

    // Send email
    $to = "ismailmakamel12@gmail.com"; // Change this to your email address
    $subject = "New message from $name";
    $body = "Name: $name\nEmail: $email\nMessage: $message";
    $headers = "From: $email";

    if (mail($to, $subject, $body, $headers)) {
        echo "Email sent successfully";
    } else {
        echo "Failed to send email";
    }
} else {
    // Handle invalid request method
    echo "Invalid request";
}
?>

document.getElementById('contactForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default form submission

    // Get form data
    var name = document.getElementById('name').value;
    var email = document.getElementById('email').value;
    var message = document.getElementById('message').value;

    // Send form data to server
    sendEmail(name, email, message);
});

function sendEmail(name, email, message) {
    var data = {
        name: name,
        email: email,
        message: message
    };

    fetch('/send_email', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => {
        if (response.ok) {
            alert('Email sent successfully');
        } else {
            alert('Failed to send email');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Failed to send email');
    });
}

Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # views.py

from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  # Disable CSRF protection for this view (for simplicity, but not recommended in production)
def send_email(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        try:
            # Send email
            send_mail(
                'Message from Website',  # Subject of the email
                f'Name: {name}\nEmail: {email}\n\nMessage: {message}',  # Email body
                'sender@example.com',  # Sender's email address
                ['recipient@example.com'],  # List of recipient email addresses
                fail_silently=False,  # Raise an exception if sending fails
            )
            return JsonResponse({'success': 'Email sent successfully'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)

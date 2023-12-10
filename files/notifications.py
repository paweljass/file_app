from django.core.mail import send_mail

def send_success_notification(uploaded_file):
    subject = 'File Upload Success'
    message = f'The file {uploaded_file.original_name} has been successfully processed.\nS3 URL: {uploaded_file.s3_url}'
    from_email = 'email@example.com'
    recipient_list = ['recipient@example.com']

    send_mail(subject, message, from_email, recipient_list)
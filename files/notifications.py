def send_success_notification(uploaded_file):
    # change to push/email/sms etc
    print(
        f"File {uploaded_file.original_name} successfully processed. S3 URL: {uploaded_file.s3_url}"
    )

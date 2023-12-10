import boto3
from botocore.exceptions import NoCredentialsError
from django.conf import settings
from celery import shared_task
from .models import UploadedFile
from .notifications import send_success_notification
from .utils import generate_s3_url
import logging


@shared_task
def process_uploaded_file(file_id, file_content):
    try:
        uploaded_file = UploadedFile.objects.get(id=file_id)

        try:
            s3 = boto3.client(
                "s3",
                aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            )
            s3.put_object(
                Bucket=settings.AWS_STORAGE_BUCKET_NAME,
                Key=uploaded_file.unique_name,
                Body=file_content,
            )

            uploaded_file.s3_url = generate_s3_url(uploaded_file.unique_name)
            uploaded_file.save()

            send_success_notification(uploaded_file)

        except NoCredentialsError:
            logging.ERROR("Authorization error: Cannot access AWS credentials")

    except UploadedFile.DoesNotExist:
        pass

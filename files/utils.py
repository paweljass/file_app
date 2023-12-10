from django.conf import settings
import uuid


def generate_unique_name():
    return str(uuid.uuid4())


def generate_s3_url(unique_name):
    return f"{settings.AWS_S3_CUSTOM_DOMAIN}/{unique_name}"

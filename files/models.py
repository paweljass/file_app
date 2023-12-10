from django.db import models


class UploadedFile(models.Model):
    file = models.FileField(null=True, upload_to="uploaded_files/")
    unique_name = models.CharField(max_length=255, unique=True)
    original_name = models.CharField(max_length=255)
    s3_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"{self.original_name} ({self.s3_url})"

    class Meta:
        verbose_name = 'Uploaded File'
        verbose_name_plural = 'Uploaded Files'
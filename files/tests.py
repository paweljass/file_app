from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import UploadedFile
from rest_framework.test import APIClient
from .tasks import process_uploaded_file
from unittest.mock import patch


class CeleryTaskTests(TestCase):
    def test_process_uploaded_file(self):
        uploaded_file = UploadedFile.objects.create(
            unique_name="test_unique_name", original_name="test_file.txt"
        )
        file_content = b"Test file content"

        with patch("your_app.tasks.generate_s3_url") as mock_generate_s3_url:
            process_uploaded_file(uploaded_file.id, file_content)

        updated_file = UploadedFile.objects.get(id=uploaded_file.id)

        self.assertIsNotNone(updated_file.s3_url)
        mock_generate_s3_url.assert_called_once_with(uploaded_file.unique_name)


class FileUploadViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_file_upload(self):
        file_content = b"Test file content"
        uploaded_file = SimpleUploadedFile("test_file.txt", file_content)

        response = self.client.post(
            "/api/upload/", {"file": uploaded_file}, format="multipart"
        )

        self.assertEqual(response.status_code, 202)

        self.assertEqual(UploadedFile.objects.count(), 1)

        with patch("your_app.tasks.process_uploaded_file.delay") as mock_task:
            self.assertEqual(mock_task.call_count, 1)

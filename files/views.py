from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UploadedFile
from .tasks import process_uploaded_file
from .utils import generate_unique_name


class FileUploadView(APIView):
    def post(self, request, *args, **kwargs):
        file = request.FILES.get("file")
        original_name = file.name
        unique_name = generate_unique_name()

        uploaded_file = UploadedFile.objects.create(
            file=None, unique_name=unique_name, original_name=original_name
        )

        process_uploaded_file.delay(uploaded_file.id, file.read())

        return Response(
            {"status": "File upload started"}, status=status.HTTP_202_ACCEPTED
        )

Django-based application that allows users to upload files to Amazon S3. Below is a brief description of how the program works and where to find key elements.

## How It Works?

1. **File Upload:**
   - Users can upload files through the API using the provided file upload URL.
   - Files are directly saved to Amazon S3, and information about the files is stored in the Django database.

2. **File Processing:**
   - Uploaded files are processed asynchronously using Celery, eliminating the need for users to wait for extended periods.
   - After processing is complete, file information is updated, and the user receives a notification (for example email).

3. **Elements:**
   - `models.py`: Contains the definition of the UploadedFile model and its fields.
   - `views.py`: Contains Django views, including the view for file uploads.
   - `tasks.py`: Contains Celery tasks, such as file processing.
   - `utils.py`: Contains utility functions, such as generating unique file names.
   - `notifications.py`: Contains functions for sending notifications.

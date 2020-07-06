from learning_django import settings
from pathlib import Path


def handle_uploaded_file(file):
    files_uploads = settings.MEDIA_ROOT + '/uploads/'
    files_uploads_dir = Path(files_uploads)

    if not files_uploads_dir.exists():
        files_uploads_dir.mkdir(0o777, False, False)

    file_url = files_uploads + str(file)
    with open(file_url, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

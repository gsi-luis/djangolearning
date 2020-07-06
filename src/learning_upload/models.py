from django.db import models


class UploadFile(models.Model):
    file = models.FileField()


class UploadFileStorage(models.Model):
    file = models.FileField(upload_to='upload_storage')

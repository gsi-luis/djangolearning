from django import forms
from .models import UploadFile, UploadFileStorage


class UploadFileForm(forms.Form):
    file = forms.FileField()


class ModelFormWithFileField(forms.ModelForm):
    class Meta:
        model = UploadFile
        fields = ['file']


class ModelFormWithStorage(forms.ModelForm):
    class Meta:
        model = UploadFileStorage
        fields = ['file']

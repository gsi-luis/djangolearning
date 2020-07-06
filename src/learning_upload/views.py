from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from .forms import UploadFileForm
from .uploads import handle_uploaded_file
from .forms import ModelFormWithFileField, ModelFormWithStorage
from .models import UploadFile, UploadFileStorage


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect(reverse('learning_upload:upload_list'))
    else:
        form = UploadFileForm()
    return render(request, 'learning_upload/upload_new.html', {'form': form})


def upload_list(request):
    from pathlib import Path
    from learning_django import settings

    uploads = Path(settings.MEDIA_ROOT+'/uploads/')
    files = []
    for file in uploads.iterdir():
        if file.is_file():
            files.append({'name': file.name})

    files_with_model = UploadFile.objects.all()
    files_with_model_storage = UploadFileStorage.objects.all()

    context = {'files': files, 'files_with_model': files_with_model, 'files_with_model_storage': files_with_model_storage}
    return render(request, 'learning_upload/upload_list.html', context)


def upload_file_with_model(request):
    if request.method == 'POST':
        form = ModelFormWithFileField(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_upload:upload_list'))
    else:
        form = ModelFormWithFileField()
    return render(request, 'learning_upload/upload_new.html', {'form': form})


def upload_file_with_model_storage(request):
    if request.method == 'POST':
        form = ModelFormWithStorage(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_upload:upload_list'))
    else:
        form = ModelFormWithFileField()
    return render(request, 'learning_upload/upload_new.html', {'form': form})

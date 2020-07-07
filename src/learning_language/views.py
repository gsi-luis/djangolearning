from django.shortcuts import render
from .forms import LanguageForm
from learning_django import settings
from django.utils import translation


def index(request):
    language_default = settings.LANGUAGE_CODE

    if request.method == "POST":
        form = LanguageForm(request.POST)
        if form.is_valid():
            language_default = request.POST['language_field']
    else:
        form = LanguageForm()

    context = {
        'form': form,
        'language_default': language_default
    }
    translation.activate(language_default)
    return render(request, 'learning_language/language_index.html', context)

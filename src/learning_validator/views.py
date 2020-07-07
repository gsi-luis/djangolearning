from django.shortcuts import render
from .forms import ValidatorCustomForm, WidgetForm
from django.http import HttpResponseRedirect
from django.urls import reverse


def index(request):
    return render(request, 'learning_validator/validator_index.html')


def validator_custom(request):
    if request.method == "POST":
        form = ValidatorCustomForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('learning_validator:validator_index'))
    else:
        form = ValidatorCustomForm()
    return render(request, 'learning_validator/validator_custom_form.html', {'form': form})


def widget_custom(request):
    form = WidgetForm()
    return render(request, 'learning_validator/validator_custom_form.html', {'form': form})

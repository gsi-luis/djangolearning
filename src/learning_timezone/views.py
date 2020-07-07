from django.shortcuts import render
import datetime
from .forms import TimeZoneChoiceForm, load_timezone_all
from learning_django import settings


def index(request):
    timezone_default = settings.TIME_ZONE

    if request.method == "POST":
        form = TimeZoneChoiceForm(request.POST)
        if form.is_valid():
            timezone_default = request.POST['timezone_field']
    else:
        form = TimeZoneChoiceForm()

    timezone_list = load_timezone_all()
    datetime_now = datetime.datetime.now()
    context = {
        'timezone_list': timezone_list,
        'datetime_now': datetime_now,
        'form': form,
        'timezone_default': timezone_default
    }
    return render(request, 'learning_timezone/timezone_list.html', context)

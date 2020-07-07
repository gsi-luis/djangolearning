from django import forms
import pytz


def load_timezone_all():
    timezones_list = []
    for tz in pytz.all_timezones:
        timezones_list.append((tz, tz))

    return timezones_list


class TimeZoneChoiceForm(forms.Form):
    timezone_field = forms.CharField(
        widget=forms.Select(choices=load_timezone_all())
    )

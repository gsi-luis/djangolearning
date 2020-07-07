from django import forms
from . import validators


class ValidatorCustomForm(forms.Form):
    number = forms.IntegerField(
        validators=[validators.validate_number],
        help_text="Enter numbers greater than or equal to 1 and less than or equal to 10."
    )


BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]


class WidgetForm(forms.Form):
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    text_area = forms.CharField(widget=forms.Textarea(attrs={'cols': 20}))
    favorite_colors = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=FAVORITE_COLORS_CHOICES,
    )

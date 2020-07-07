from django import forms


LANGUAGES_CODE = [
    ('es', 'Español'),
    ('en', 'Ingles'),
]


class LanguageForm(forms.Form):
    language_field = forms.CharField(
        widget=forms.Select(choices=LANGUAGES_CODE)
    )

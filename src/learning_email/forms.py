from django import forms


class SendEmailForm(forms.Form):
    subject = forms.CharField(max_length=150)
    message = forms.CharField(max_length=350, widget=forms.Textarea(attrs={'rows': 20}))
    email_to = forms.EmailField(max_length=50, widget=forms.EmailInput())

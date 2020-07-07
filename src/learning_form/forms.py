from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super(PostForm, self).clean()
        title = cleaned_data.get("title")
        text = cleaned_data.get("text")
        if title == text:
            raise forms.ValidationError("You value for 'title' and 'text' is not equal.")

    def clean_title(self):
        data = self.cleaned_data['title']

        if len(data) < 5:
            raise forms.ValidationError("You have characters greater than 4 characters.")
        elif len(data) > 150:
            raise forms.ValidationError("You have characters less than 150 characters.")

        return data

    def clean_text(self):
        data = self.cleaned_data['text']

        if len(data) < 5:
            raise forms.ValidationError("You have characters greater than 4 characters.")
        elif len(data) > 250:
            raise forms.ValidationError("You have characters less than 250 characters.")

        return data

    class Meta:
        model = Post
        fields = ('title', 'text', )
        #exclude = ('title',)


class CustomFieldParametersForm(forms.Form):
    subject = forms.CharField(max_length=100, help_text='100 characters max.')
    message = forms.CharField()
    sender = forms.EmailField(help_text='A valid email address, please.')
    cc_myself = forms.BooleanField(required=False)

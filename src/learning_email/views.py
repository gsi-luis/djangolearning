from django.shortcuts import render
from .forms import SendEmailForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core import mail
from decouple import config


def index(request):
    if request.method == "POST":
        form = SendEmailForm(request.POST)
        if form.is_valid():
            subject = request.POST['subject']
            message = request.POST['message']
            email_to = request.POST['email_to']

            connection = mail.get_connection()
            mail.send_mail(
                subject,
                message,
                config('EMAIL_HOST_USER'),
                [email_to],
                fail_silently=False
            ).send()

            return HttpResponseRedirect(reverse('learning_email:email_index'))
    else:
        form = SendEmailForm()
    context = {'form': form }
    return render(request, 'learning_email/email_index.html', context)

from django.shortcuts import render
from decouple import config


def index(request):
    context = {'config': {
        'DEBUG': config('DEBUG'),
        'DJANGO_ALLOWED_HOSTS': config('DJANGO_ALLOWED_HOSTS'),
        'SQL_ENGINE': config('SQL_ENGINE'),
        'SQL_DATABASE': config('SQL_DATABASE'),
        'SQL_USER': config('SQL_USER'),
        'SQL_HOST': config('SQL_HOST'),
    }}
    return render(request, 'learning_env/env_index.html', context)

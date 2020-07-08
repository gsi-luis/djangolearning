from django.conf.urls import url
from . import views

app_name = 'learning_email'

urlpatterns = [
    url(r'^$', views.index, name='email_index'),
]
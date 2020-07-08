from django.conf.urls import url
from . import views

app_name = 'learning_log'

urlpatterns = [
    url(r'^$', views.index, name='log_index'),
]
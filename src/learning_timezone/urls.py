from django.conf.urls import url
from . import views

app_name = 'learning_timezone'

urlpatterns = [
    url(r'^$', views.index, name='timezone_index'),
]

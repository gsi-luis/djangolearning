from django.conf.urls import url
from . import views

app_name = 'learning_env'

urlpatterns = [
    url(r'^$', views.index, name='env_index'),
]
from django.conf.urls import url
from . import views

app_name = 'learning_language'

urlpatterns = [
    url(r'^$', views.index, name='language_index'),
]
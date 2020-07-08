from django.conf.urls import url
from . import views

app_name = 'learning_asyncio'

urlpatterns = [
    url(r'^$', views.index, name='asyncio_index'),
    url(r'^show_asyncio_data$', views.show_data_csv, name='asyncio_show'),
]
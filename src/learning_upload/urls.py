from django.conf.urls import url
from . import views

app_name = 'learning_upload'

urlpatterns = [
    url(r'^$', views.upload_list, name='upload_list'),
    url(r'^new/$', views.upload_file, name='upload_new'),
    url(r'^new_with_model/$', views.upload_file_with_model, name='upload_new_with_model'),
    url(r'^new_with_model_storage/$', views.upload_file_with_model_storage, name='upload_new_with_model_storage'),
]

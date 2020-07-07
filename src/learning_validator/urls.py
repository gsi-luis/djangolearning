from django.conf.urls import url
from . import views


app_name = 'learning_validator'


urlpatterns = [
    url(r'^$', views.index, name='validator_index'),
    url(r'^validator_custom', views.validator_custom, name='validator_custom'),
    url(r'^widget_custom', views.widget_custom, name='widget_custom'),
]

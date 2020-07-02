from django.conf.urls import url
from . import views

app_name = 'polls'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

    # View generic django
    url(r'^generic$', views.IndexView.as_view(), name='generic_index'),
    url(r'^generic/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='generic_detail'),
    url(r'^generic/(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='generic_results'),
]

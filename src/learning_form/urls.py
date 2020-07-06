from django.conf.urls import url
from . import views

app_name = 'learning_form'

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),

    url(r'^author/create/$', views.AuthorCreate.as_view(), name='author_create'),
    url(r'^author/$', views.AuthorListView.as_view(), name='author_list'),
    url(r'^author/(?P<pk>\d+)/$', views.AuthorDetailView.as_view(), name='author_detail'),
    url(r'^author/(?P<pk>\d+)/update/$', views.AuthorUpdate.as_view(), name='author_update'),
    url(r'^author/(?P<pk>\d+)/delete/$', views.AuthorDelete.as_view(), name='author_delete'),
]

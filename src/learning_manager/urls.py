from django.conf.urls import url
from . import views

app_name = 'learning_manager'

urlpatterns = [
    # View generic django
    url(r'^$', views.IndexPersonsView.as_view(), name='index_persons'),
    url(r'^editors/$', views.IndexEditorView.as_view(), name='index_editors'),
    url(r'^authors/$', views.IndexAuthorView.as_view(), name='index_authors'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailPersonView.as_view(), name='detail_person'),
]

from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from learning_search_indexes.viewsets.book import BookDocumentView
from learning_search_indexes.viewsets.tag import TagDocumentView


router = DefaultRouter()
books = router.register(r'books', BookDocumentView, basename='bookdocument')
books = router.register(r'tag', TagDocumentView, basename='tagdocument')

app_name = 'learning_search_indexes'

urlpatterns = [
    url(r'^', include(router.urls)),
]

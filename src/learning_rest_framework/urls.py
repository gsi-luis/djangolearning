from django.urls import include, path
from rest_framework import routers, renderers
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


app_name = 'learning_rest_framework'

router = routers.DefaultRouter()
router.register(r'groups', views.GroupViewSet)

snippet_list = views.SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
snippet_detail = views.SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
snippet_highlight = views.SnippetViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])
user_list = views.UserViewSet.as_view({
    'get': 'list'
})
user_detail = views.UserViewSet.as_view({
    'get': 'retrieve'
})

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('snippets/', snippet_list, name='snippet-list'),
    path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
    path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
    path('users/', user_list, name='user-list'),
    path('users/<int:pk>/', user_detail, name='user-detail'),
    path('manual/snippets/', views.snippet_list),
    path('manual/snippets/<int:pk>/', views.snippet_detail),
    path('api_view/snippets/', views.SnippetList.as_view()),
    path('api_view/snippets/<int:pk>/', views.SnippetDetail.as_view()),
    path('mixin/snippets/', views.SnippetMixinList.as_view()),
    path('mixin/snippets/<int:pk>/', views.SnippetMixinDetail.as_view()),
    path('generic/snippets/', views.SnippetGenericList.as_view()),
    path('generic/snippets/<int:pk>/', views.SnippetGenericDetail.as_view()),
    path('permission/snippets/', views.SnippetPermissionList.as_view()),
    path('permission/snippets/<int:pk>/', views.SnippetPermissionDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns.append(path('', include(router.urls)))


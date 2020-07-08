"""learning_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='main_index'),
    path('polls/', include('polls.urls')),
    path('persons/', include('learning_manager.urls')),
    path('upload/', include('learning_upload.urls')),
    path('form/', include('learning_form.urls')),
    path('pdf/', include('learning_wkhtmltopdf.urls')),
    path('validator/', include('learning_validator.urls')),
    path('timezone/', include('learning_timezone.urls')),
    path('language/', include('learning_language.urls')),
    path('log/', include('learning_log.urls')),
    path('email/', include('learning_email.urls')),
    path('env/', include('learning_env.urls')),
    path('asyncio/', include('learning_asyncio.urls')),
    path('rest/', include('learning_rest_framework.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
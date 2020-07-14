from django.conf.urls import url
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(
    title='Learning django API',
    renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer]
)

app_name = 'learning_swager'

urlpatterns = [
    url(r'^$', schema_view)
]

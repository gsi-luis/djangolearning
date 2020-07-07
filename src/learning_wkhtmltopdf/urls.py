from django.conf.urls import url
from wkhtmltopdf.views import PDFTemplateView
from . import views


app_name = 'learning_wkhtmltopdf'


urlpatterns = [
    url(r'^$', views.index, name='pdf_index'),
    url(r'^generate_simple_pdf$', PDFTemplateView.as_view(
        template_name='learning_wkhtmltopdf/simple_pdf.html', filename='my_pdf.pdf'
    ), name='generate_pdf_simple'),
    # url(r'^new/$', views.upload_file, name='upload_new'),
]

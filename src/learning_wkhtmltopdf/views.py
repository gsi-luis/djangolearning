from django.shortcuts import render


def index(request):
    return render(request, 'learning_wkhtmltopdf/pdf_index.html')

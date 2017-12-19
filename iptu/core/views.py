from django.shortcuts import render

from iptu.core.tasks import create_db_iptu


def home(request):
    return render(request, 'index.html')


def create_file(request):
    create_db_iptu.delay()
    return render(request, 'create_file.html')

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'galeria/index.html')


def outro(request):
    return render(request, 'galeria/outro.html')


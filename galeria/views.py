from django.shortcuts import render
from django.http import HttpResponse

from galeria.dados_teste import dados

def index(request):

    cards = dados

    return render(request, 'galeria/index.html', { 'cards': cards })


def outro(request):
    return render(request, 'galeria/outro.html')


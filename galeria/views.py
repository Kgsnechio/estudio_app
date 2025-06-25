from django.shortcuts import render
from django.http import HttpResponse

from galeria.models import ArtigoGaleria

def index(request):

    cards = ArtigoGaleria.objects.all()
    print(cards)

    return render(request, 'galeria/index.html', { 'cards': cards })


def outro(request):

    return render(request, 'galeria/outro.html')


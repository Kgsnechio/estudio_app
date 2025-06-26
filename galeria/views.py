from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from galeria.models import ArtigoGaleria
from django.db.models import Q

def index(request):

    cards = ArtigoGaleria.objects.filter(publicado=True).order_by('datahora').all()

    return render(request, 'galeria/index.html', { 'cards': cards })

def artigo(request, artigo_id):

    artigo = get_object_or_404(ArtigoGaleria, pk=artigo_id)

    return render(request, 'galeria/artigo.html', { 'artigo': artigo })

def outro(request):
    return render(request, 'galeria/outro.html')

def buscar(request):

    if "buscar" in request.GET:
        buscar = request.GET['buscar']
        cards = ArtigoGaleria.objects.filter(
            Q(publicado=True) & (
            Q(nome__contains=buscar) |
            Q(titulo__contains=buscar) |
            Q(legenda__contains=buscar) 
        )).order_by('datahora').all()
        return render(request, 'galeria/buscar.html', { 'cards': cards })

    return render(request, 'galeria/buscar.html')
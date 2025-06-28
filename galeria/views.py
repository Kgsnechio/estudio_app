from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from galeria.models import ArtigoGaleria
from django.db.models import Q

from django.contrib import messages

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Por favor, efetue o login.')
        return redirect('login')

    cards = ArtigoGaleria.objects.filter(publicado=True).order_by('datahora').all()

    return render(request, 'galeria/index.html', { 'cards': cards })

def artigo(request, artigo_id):
    if not request.user.is_authenticated:
        messages.error(request, 'Por favor, efetue o login.')
        return redirect('login')

    artigo = get_object_or_404(ArtigoGaleria, pk=artigo_id)

    return render(request, 'galeria/artigo.html', { 'artigo': artigo })

def outro(request):

    if ArtigoGaleria.objects.exists():
        return render(request, 'galeria/outro.html')

    from .dados_teste import dados 

    cards = dados

    for i, card in cards.items():
        new_artigo = ArtigoGaleria(**card)
        new_artigo.save()

    return render(request, 'galeria/outro.html')

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Por favor, efetue o login.')
        return redirect('login')

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
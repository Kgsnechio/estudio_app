from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from galeria.models import ArtigoGaleria

def index(request):

    cards = ArtigoGaleria.objects.filter(publicado=True).order_by('datahora').all()

    return render(request, 'galeria/index.html', { 'cards': cards })

def artigo(request, artigo_id):

    artigo = get_object_or_404(ArtigoGaleria, pk=artigo_id)

    return render(request, 'galeria/artigo.html', { 'artigo': artigo })

def outro(request):
    return render(request, 'galeria/outro.html')
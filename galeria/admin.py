from django.contrib import admin
from galeria.models import ArtigoGaleria, CategoriaArtigoGaleria

# Register your models here.

class ListarArtigosGaleria(admin.ModelAdmin):
    list_display = ('id', 'nome', 'titulo', 'categoria', 'publicado')
    list_display_links = ('id', 'nome', 'titulo')
    search_fields = ('id', 'nome', 'legenda', 'image_path', 'titulo', 'artigo', 'categoria', 'publicado')
    list_filter = ('categoria', 'publicado')
    list_editable = ('categoria', 'publicado')
    list_per_page = 25

admin.site.register(ArtigoGaleria, ListarArtigosGaleria)

class ListarCategoriaArtigoGaleria(admin.ModelAdmin):
    list_display = ('id', 'nome', 'descricao')
    list_display_links = ('id', 'nome', 'descricao')
    search_fields = ('id', 'nome', 'descricao')
    list_per_page = 25

admin.site.register(CategoriaArtigoGaleria, ListarCategoriaArtigoGaleria)
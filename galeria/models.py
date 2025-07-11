from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
class CategoriaArtigoGaleria(models.Model):
    nome = models.CharField(max_length=255, unique=True)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome

class ArtigoGaleria(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    legenda = models.TextField(blank=True, null=True)
    imagem_path = models.TextField(blank=True, null=True)
    imagem = models.ImageField(upload_to='galeria/%Y/%m/%d', blank=True, null=True)
    titulo = models.TextField(blank=True, null=True)
    artigo = models.TextField(blank=True, null=True)
    categoria = models.ForeignKey(CategoriaArtigoGaleria, on_delete=models.SET_NULL, null=True, blank=True)
    publicado = models.BooleanField(default=False)
    datahora = models.DateTimeField(default=datetime.now, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=False, related_name='user')

    def __init__(self, *args, **kwargs):
        nome = kwargs.pop('nome', None)
        legenda = kwargs.pop('legenda', None)
        imagem_path = kwargs.pop('imagem_path', None)
        titulo = kwargs.pop('titulo', None)
        artigo = kwargs.pop('artigo', None)

        super().__init__(*args, **kwargs)

        if nome is not None:
            self.nome = nome
        if legenda is not None:
            self.legenda = legenda
        if imagem_path is not None:
            self.imagem_path = imagem_path
        if titulo is not None:
            self.titulo = titulo
        if artigo is not None:
            self.artigo = artigo

        self.publicado = True

    def __str__(self):
        return f'{self.nome} - {self.titulo}'
    
    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'legenda': self.legenda,
            'image_path': self.image_path,
            'titulo': self.titulo,
            'artigo': self.artigo,
            'categoria': self.categoria
        }
        
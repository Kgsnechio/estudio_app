from django.db import models

# Create your models here.
class ArtigoGaleria(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    legenda = models.TextField(blank=True, null=True)
    image_path = models.TextField(blank=True, null=True)
    titulo = models.TextField(blank=True, null=True)
    artigo = models.TextField(blank=True, null=True)

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
        }
        
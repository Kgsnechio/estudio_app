from django.urls import path
from galeria.views import index, outro, artigo

urlpatterns = [
    path('', index, name='index'),
    path('outro/', outro, name='outro'),
    path('artigo/<int:artigo_id>', artigo, name='artigo'),
]
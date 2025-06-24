from django.urls import path
from galeria.views import index, outro

urlpatterns = [
    path('', index, name='index'),
    path('outro/', outro, name='outro'),
]
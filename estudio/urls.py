from django.urls import path
from estudio.views import home

urlpatterns = [
    path('home', home, name='home'),
]
from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name="home"),
    path('crear', crear_favoritos, name="crear"),
    path('lista', lista_favoritos, name="lista"),
]

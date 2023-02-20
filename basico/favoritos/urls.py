from django.urls import path
from .views import *

app_name = 'favs'

urlpatterns = [
    path('', index, name="home"),
    path('crear', crear_favoritos, name="crear"),
    path('lista', lista_favoritos, name="lista"),
    path('borrar/<int:pk>', borrar_favoritos, name="borrar"),
]
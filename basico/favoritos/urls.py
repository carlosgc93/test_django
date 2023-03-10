from django.urls import path
from .views import *

app_name = 'favs'

urlpatterns = [
    path('', index, name="home"),
    path('crear', crear_favoritos, name="crear"),
    path('lista', lista_favoritos, name="lista"),
    path('borrar/<int:pk>', borrar_favoritos, name="borrar"),
    path('detalle/<int:pk>', detalle_favoritos, name="detalle"),
    path('actualizar/<int:pk>', actualizar_favoritos, name="actualizar"),
]
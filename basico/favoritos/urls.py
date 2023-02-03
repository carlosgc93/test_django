from django.urls import path
from .views import *

app_name='favoritos'

urlpatterns = [
    path('',index),
    path('crear',crear_favoritos),
    path('lista',lista_favoritos),
]
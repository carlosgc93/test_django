from django.shortcuts import render, redirect
from .models import Favoritos
from .forms import FavoritoModelForm
from django.urls import reverse

# Create your views here.


def index(request):
    return render(request, 'index.html')


def crear_favoritos(request):

    form = FavoritoModelForm()

    if request.method == 'POST':
        form = FavoritoModelForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('favs:lista')
        else:
            print(form.errors)

    context = {
        'form': form
    }

    return render(request, 'favoritos/crear.html', context)


def lista_favoritos(request):

    favoritos_lista = Favoritos.objects.all()

    context = {
        'favoritos_lista': favoritos_lista
    }

    return render(request, 'favoritos/lista.html', context)


def borrar_favoritos(request, pk):
    Favoritos.objects.get(pk=pk).delete()
    return redirect('favs:lista')

from django.shortcuts import render
from .models import Favoritos
from .forms import FavoritoForm

# Create your views here.


def index(request):
    return render(request, 'index.html')


def crear_favoritos(request):

    form = FavoritoForm()

    if request.method == 'POST':
        form = FavoritoForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            url = form.cleaned_data['url']
            Favoritos.objects.create(nombre=nombre, url=url)

    context = {
        'form': form
    }

    return render(request, 'favoritos/crear.html', context)


def lista_favoritos(request):
    return render(request, 'favoritos/lista.html')

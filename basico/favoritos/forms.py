from django import forms
from .models import Favoritos

# opcion de formulario uno


class FavoritoForm(forms.Form):
    nombre = forms.CharField()
    url = forms.URLField()


# formulario version dos mas pro
class FavoritoModelForm(forms.ModelForm):
    class Meta:
        model= Favoritos
        fields = '__all__' # ['nombre']
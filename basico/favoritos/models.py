from django.db import models

# Create your models here.


class Favoritos(models.Model):
    nombre = models.CharField(max_length=200, blank=True)
    url = models.URLField()

    # para mostrar el nombre del objeto
    def __str__(self):
        return self.nombre

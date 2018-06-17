from django.contrib import admin

# Register your models here.

from .models import Autor,Gatunek,Ksiazka,InstancjaKsiazki

admin.site.register(Autor)
admin.site.register(Gatunek)
admin.site.register(Ksiazka)
admin.site.register(InstancjaKsiazki)
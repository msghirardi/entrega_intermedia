from django.contrib import admin
from blog.models import Autor, Seccion, Articulo

# Register your models here.
admin.site.register(Articulo)
admin.site.register(Seccion)
admin.site.register(Autor)

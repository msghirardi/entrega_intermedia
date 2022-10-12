from django.urls import path, include
from blog.views import (
    procesar_formulario_articulo,
    procesar_formulario_autor,
    procesar_formulario_seccion,
    buscar,
    mostrar_inicio,
)

urlpatterns = [
    path(
        "formulario-articulo/",
        procesar_formulario_articulo,
    ),
    path("formulario-seccion/", procesar_formulario_seccion),
    path("formulario-autor/", procesar_formulario_autor),
    path("buscar-articulo/", buscar),
    path("inicio/", mostrar_inicio),
]

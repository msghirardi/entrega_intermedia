from django.http import HttpResponse
from django.shortcuts import render

from blog.forms import ArticuloForm, SeccionForm, AutorForm

# Create your views here.


def procesar_formulario_articulo(request) -> HttpResponse:
    mi_formulario = ArticuloForm()
    contexto = {"formulario": mi_formulario}

    return HttpResponse(contexto)


def procesar_formulario_autor(request):
    mi_formulario = AutorForm()
    contexto = {"formulario": mi_formulario}
    return render(request, "blog/formulario-autor.html", contex=contexto)


def procesar_formulario_seccion(request):
    mi_formulario = SeccionForm()
    contexto = {"formulario": mi_formulario}
    return render(request, "blog/formulario-seccion.html", contex=contexto)

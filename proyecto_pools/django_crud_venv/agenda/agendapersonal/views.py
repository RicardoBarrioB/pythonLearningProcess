from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Entrada, Actualizacion

class Index(generic.ListView):
    template_name = 'agendapersonal/index.html'
    context_object_name = 'latest_entrada_list'

    def get_queryset(self):
        return Entrada.objects.order_by('fecha_creacion')


class VistaDetalles(generic.DeleteView):
    model = Entrada
    template_name = 'agendapersonal/detalles.html'

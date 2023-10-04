from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Pregunta
from django.urls import reverse_lazy

class PreguntaListView(ListView):
    model = Pregunta
    template_name = 'preguntas/pregunta_list.html'  # Cambia esto al nombre de tu plantilla
    context_object_name = 'preguntas'

class PreguntaDetailView(DetailView):
    model = Pregunta
    template_name = 'preguntas/pregunta_detail.html'  # Cambia esto al nombre de tu plantilla
    context_object_name = 'pregunta'

class PreguntaCreateView(CreateView):
    model = Pregunta
    template_name = 'preguntas/pregunta_form.html'  # Cambia esto al nombre de tu plantilla
    fields = ['texto', 'categoria']  # Agrega los campos que necesites
    success_url = reverse_lazy('pregunta-list')

class PreguntaUpdateView(UpdateView):
    model = Pregunta
    template_name = 'preguntas/pregunta_update.html'  # Cambia esto al nombre de tu plantilla
    fields = ['texto', 'categoria']  # Agrega los campos que necesites

    def get_success_url(self):
        return reverse_lazy('pregunta-detail', kwargs={'pk': self.object.pk})

class PreguntaDeleteView(DeleteView):
    model = Pregunta
    template_name = 'preguntas/pregunta_delete.html'  # Cambia esto al nombre de tu plantilla
    success_url = reverse_lazy('pregunta-list')

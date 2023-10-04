from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Trivia
from django.urls import reverse_lazy

class TriviaListView(ListView):
    model = Trivia
    template_name = 'trivias/trivia_list.html'  # Cambia esto al nombre de tu plantilla
    context_object_name = 'trivias'

class TriviaDetailView(DetailView):
    model = Trivia
    template_name = 'trivias/trivia_detail.html'  # Cambia esto al nombre de tu plantilla
    context_object_name = 'trivia'

class TriviaCreateView(CreateView):
    model = Trivia
    template_name = 'trivias/trivia_create.html'  # Cambia esto al nombre de tu plantilla
    fields = ['titulo','nivel','user']  # Agrega los campos que necesites
    success_url = reverse_lazy('trivia-list')

class TriviaUpdateView(UpdateView):
    model = Trivia
    template_name = 'trivias/trivia_update.html'  # Cambia esto al nombre de tu plantilla
    fields = ['titulo', 'nivel', 'user']  # Agrega los campos que necesites

    def get_success_url(self):
        return reverse_lazy('trivia-detail', kwargs={'pk': self.object.pk})

class TriviaDeleteView(DeleteView):
    model = Trivia
    template_name = 'trivias/trivia_delete.html'  # Cambia esto al nombre de tu plantilla
    success_url = reverse_lazy('trivia-list')

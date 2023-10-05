from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Pregunta, Respuesta # Importa el modelo Respuesta
from django.urls import reverse_lazy

class PreguntaListView(ListView):
    model = Pregunta
    template_name = 'preguntas/pregunta_list.html'
    context_object_name = 'preguntas'

class PreguntaDetailView(DetailView):
    model = Pregunta
    template_name = 'preguntas/pregunta_detail.html'
    context_object_name = 'pregunta'

class PreguntaCreateView(CreateView):
    model = Pregunta
    template_name = 'preguntas/pregunta_form.html'
    fields = ['texto', 'categoria']
    success_url = reverse_lazy('pregunta-list')

class PreguntaUpdateView(UpdateView):
    model = Pregunta
    template_name = 'preguntas/pregunta_update.html'
    fields = ['texto', 'categoria']  # No incluyas 'respuestas' aquí

    def form_valid(self, form):
        pregunta = form.save(commit=False)
        
        respuestas_seleccionadas = self.request.POST.getlist('respuestas')
        pregunta.actualizar_respuestas(respuestas_seleccionadas)

        pregunta.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('pregunta-detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['respuestas_disponibles'] = Respuesta.objects.all()
        return context


class PreguntaDeleteView(DeleteView):
    model = Pregunta
    template_name = 'preguntas/pregunta_delete.html'
    success_url = reverse_lazy('pregunta-list')
    
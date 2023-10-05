from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Trivia
from django.http import JsonResponse
from django.views import View
from preguntas.models import Pregunta, Respuesta
from django.urls import reverse_lazy

class TriviaListView(ListView):
    model = Trivia
    template_name = 'trivias/trivia_list.html'
    context_object_name = 'trivias'

class TriviaDetailView(DetailView):
    model = Trivia
    template_name = 'trivias/trivia_detail.html'
    context_object_name = 'trivia'

class TriviaCreateView(CreateView):
    model = Trivia
    template_name = 'trivias/trivia_create.html'
    fields = ['titulo', 'user', 'nivel', 'preguntas']  # Añade el campo 'preguntas'
    success_url = reverse_lazy('trivia-list')

    def form_valid(self, form):
        trivia = form.save(commit=False)
        trivia.save()
        form.save_m2m()  # Guarda las relaciones ManyToMany
        return redirect('trivia-list')

class TriviaUpdateView(UpdateView):
    model = Trivia
    template_name = 'trivias/trivia_update.html'
    fields = ['titulo', 'nivel', 'preguntas']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        trivia = self.get_object()
        preguntas_seleccionadas = trivia.preguntas.all().values_list('pk', flat=True)
        context['preguntas_seleccionadas'] = preguntas_seleccionadas
        return context

    def get_success_url(self):
        return reverse_lazy('trivia-detail', kwargs={'pk': self.object.pk})

class TriviaDeleteView(DeleteView):
    model = Trivia
    template_name = 'trivias/trivia_delete.html'
    success_url = reverse_lazy('trivia-list')

class JugarTriviaView(View):
    template_name = 'trivias/jugar_trivia.html'

    def get(self, request):
        # Obtén la lista de trivias disponibles para que el usuario seleccione una
        trivias_disponibles = Trivia.objects.all()
        return render(request, self.template_name, {'trivias_disponibles': trivias_disponibles})

    def post(self, request):
        # Obtén la trivia seleccionada por el usuario desde el formulario
        trivia_id = request.POST.get('trivia_id')
        trivia = get_object_or_404(Trivia, pk=trivia_id)

        # Obtén las preguntas de la trivia seleccionada
        preguntas = Pregunta.objects.filter(trivia=trivia)
        pregunta_actual = 0
        puntaje = 0

        # Verifica si el usuario ha seleccionado una respuesta en el formulario
        respuesta_seleccionada = request.POST.get('respuesta', None)
        if respuesta_seleccionada is not None:
            respuesta_seleccionada = int(respuesta_seleccionada)

            # Obtén la pregunta actual
            pregunta = preguntas[pregunta_actual]

            # Verifica si la respuesta seleccionada es correcta
            if Respuesta.objects.filter(pk=respuesta_seleccionada, pregunta=pregunta, correcta=True).exists():
                puntaje += 1

            # Avanza a la siguiente pregunta
            pregunta_actual += 1

        # Si todas las preguntas se han respondido, muestra el resultado
        if pregunta_actual >= len(preguntas):
            return render(request, 'trivias/resultado.html', {'puntaje': puntaje})

        # Obtiene la siguiente pregunta
        pregunta = preguntas[pregunta_actual]
        respuestas = Respuesta.objects.filter(pregunta=pregunta)

        return render(request, self.template_name, {
            'trivia': trivia,
            'pregunta': pregunta,
            'respuestas': respuestas,
            'pregunta_actual': pregunta_actual,
            'puntaje': puntaje,
        })
        
def obtener_preguntas_respuestas(request, trivia_id):
    # Obtén la trivia seleccionada o devuelve un error 404 si no existe
    trivia = get_object_or_404(Trivia, pk=trivia_id)

    # Obtén las preguntas relacionadas con la trivia seleccionada
    preguntas = trivia.preguntas.all()

    # Crea una lista para almacenar las preguntas y sus respuestas
    preguntas_respuestas = []

    # Itera a través de las preguntas y obtén sus respuestas
    for pregunta in preguntas:
        respuestas = pregunta.respuestas.all().values('texto', 'correcta')
        preguntas_respuestas.append({
            'pregunta': pregunta.texto,
            'respuestas': list(respuestas)
        })

    # Devuelve los datos como una respuesta JSON
    return JsonResponse(preguntas_respuestas, safe=False)
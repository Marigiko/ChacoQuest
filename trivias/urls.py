from django.urls import path
from . import views

urlpatterns = [
    # Ruta para listar todas las trivias
    path('trivias/', views.TriviaListView.as_view(), name='trivia-list'),

    # Ruta para ver los detalles de una trivia específica
    path('trivias/<int:pk>/', views.TriviaDetailView.as_view(), name='trivia-detail'),

    # Ruta para crear una nueva trivia
    path('trivias/create/', views.TriviaCreateView.as_view(), name='trivia-create'),

    # Ruta para actualizar una trivia existente
    path('trivias/<int:pk>/update/', views.TriviaUpdateView.as_view(), name='trivia-update'),

    # Ruta para eliminar una trivia existente
    path('trivias/<int:pk>/delete/', views.TriviaDeleteView.as_view(), name='trivia-delete'),
    
    # Ruta para jugar a una trivia existente
    path('jugar-trivia/', views.JugarTriviaView.as_view(), name='jugar-trivia'),
    
    path('obtener_preguntas_respuestas/<int:trivia_id>/', views.obtener_preguntas_respuestas, name='obtener_preguntas_respuestas'),
]


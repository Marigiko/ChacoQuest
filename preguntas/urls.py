from django.urls import path
from . import views

urlpatterns = [
    # Ruta para listar todas las preguntas
    path('preguntas/', views.PreguntaListView.as_view(), name='pregunta-list'),

    # Ruta para ver los detalles de una pregunta específica
    path('preguntas/<int:pk>/', views.PreguntaDetailView.as_view(), name='pregunta-detail'),

    # Ruta para crear una nueva pregunta
    path('preguntas/create/', views.PreguntaCreateView.as_view(), name='pregunta-create'),

    # Ruta para actualizar una pregunta existente
    path('preguntas/<int:pk>/update/', views.PreguntaUpdateView.as_view(), name='pregunta-update'),

    # Ruta para eliminar una pregunta existente
    path('preguntas/<int:pk>/delete/', views.PreguntaDeleteView.as_view(), name='pregunta-delete'),
]

from django.db import models
from django.contrib.auth.models import User
from preguntas.models import Pregunta

class Trivia(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    nivel = models.CharField(max_length=100)
    fecha = models.DateTimeField('fecha de creación', auto_now_add=True, editable=False)
    preguntas = models.ManyToManyField(Pregunta, related_name='trivias')

    def __str__(self):
        return f"Trivia de {self.user.username} - Nivel {self.nivel}"

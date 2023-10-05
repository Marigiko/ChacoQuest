from django.db import models

class Pregunta(models.Model):
    texto = models.CharField(max_length=200)
    categoria = models.CharField(max_length=100)
    fecha_publicacion = models.DateTimeField('fecha de publicación', null=True, blank=True)

    def __str__(self):
        return self.texto

    def cant_rtas(self):
        # Accede a las respuestas relacionadas y cuenta cuántas son
        return self.respuestas.count()

    def cant_rtas_ok(self):
        # Filtra las respuestas relacionadas que son correctas y cuenta cuántas son
        return self.respuestas.filter(correcta=True).count()
    
    def actualizar_respuestas(self, respuesta_ids):
        nuevas_respuestas = Respuesta.objects.filter(pk__in=respuesta_ids)
        self.respuestas.set(nuevas_respuestas)

class Respuesta(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE, related_name='respuestas')
    texto = models.CharField(max_length=200)
    correcta = models.BooleanField(default=False)

    def __str__(self):
        return self.texto

    def short(self):
        return self.texto[:50]  # Retorna los primeros 50 caracteres de la respuesta

    def cant_rtas_ok(self):
        return self.pregunta.respuestas.filter(correcta=True).count()

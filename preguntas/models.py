from django.db import models

class Pregunta(models.Model):
    texto = models.CharField(max_length=200)
    categoria = models.CharField(max_length=100)
    fecha_publicacion = models.DateTimeField('fecha de publicación', null=True, blank=True)

    def __str__(self):
        return self.texto

    def cant_rtas(self):
        return self.respuesta_set.count()

    def cant_rtas_ok(self):
        return self.respuesta_set.filter(correcta=True).count()

class Respuesta(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    texto = models.CharField(max_length=200)
    correcta = models.BooleanField(default=False)

    def __str__(self):
        return self.texto

    def short(self):
        return self.texto[:50]  # Retorna los primeros 50 caracteres de la respuesta

    def cant_rtas_ok(self):
        return self.respuesta_set.filter(correcta=True).count()

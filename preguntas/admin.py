from django.contrib import admin
from .models import Pregunta, Respuesta

class RespuestaInline(admin.TabularInline):
    model = Respuesta
    extra = 4

@admin.register(Pregunta)
class PreguntaAdmin(admin.ModelAdmin):
    inlines = [RespuestaInline]
    list_display = ["texto", "categoria", "cant_rtas", "cant_rtas_ok"]
    search_fields = ["texto"]
    list_filter = ["categoria"]
    ordering = ["id"]
    list_per_page = 8

@admin.register(Respuesta)
class RespuestaAdmin(admin.ModelAdmin):
    list_display = ["texto", "short", "correcta"]
    list_filter = ["correcta"]
    list_per_page = 9

admin.site.site_header = "Trivia Chaco 2021 | Admin Ver 1.0.0"
admin.site.index_title = "Trivia Chaco 2021 | Admin Dashboard"

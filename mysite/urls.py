from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import urls as auth_urls  # Cambio de alias para evitar conflicto
from trivias import urls as trivias_urls  # Cambio de alias para evitar conflicto
from preguntas import urls as preguntas_urls
from .views import HomePageView, SignUpView

urlpatterns = [
    path('', include(auth_urls)),  # Incluir las URLs de autenticación
    path('signup', SignUpView.as_view(), name='signup'),
    path('home', HomePageView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('trivia/', include(trivias_urls)),  # Incluir las URLs de la aplicación 'trivias'
    path('pregunta/', include(preguntas_urls)),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

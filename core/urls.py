from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

# No arquivo views.py do seu app Django
import logging
from django.http import JsonResponse

# Obtenha o logger configurado
logger = logging.getLogger('requestlogs')

def test_logging_view(request):
    try:
        data = {'user': 'leticia', 'email': 'leticia@contato.com'}
        # Força um erro proposital para testar o log
        raise ValueError("Erro simulado no envio de email")
    except Exception as e:
        # Loga o erro usando o logger configurado
        logger.error(f"{str(e)} | {str(data)}")
        return JsonResponse({"status": "error", "message": "Ocorreu um erro."})


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('english/', include('english.urls')),
    path('portugues/', include('portugues.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG: # update 03/11/2024: (em homologa com debug true adiciona rota static)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
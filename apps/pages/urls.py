from django.urls import path
from pages import views

urlpatterns = [
    path('', views.entrada, name='entrada'),
    path('entrou/', views.entrou, name='entrou'),
]

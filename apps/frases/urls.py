from django.urls import path
from frases import views

urlpatterns = [
    path('', views.frases, name='frases'),

]
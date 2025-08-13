from django.urls import path
from portugues import views

urlpatterns = [
    path('', views.portugues_main, name='portugues_main'),
    path('tapas01/', views.tapas01, name='tapas01'),
    path('tapas02/', views.tapas02, name='tapas02'),
    path('tapas03/', views.tapas03, name='tapas03'),
]
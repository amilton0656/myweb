from django.urls import path
from django.contrib.auth.views import LoginView
from .views import home, login_view, geral, do_logout  # Agora o 'home' existe
from django.shortcuts import render

urlpatterns = [
    path('', home, name='home'),
    path(
        "login/",
        LoginView.as_view(template_name="registration/login.html"),
        name="login"
    ),
    path("logout/", do_logout, name="logout"),

    # Rotas para as telas principais
    # path('portugues/', lambda r: render(r, 'portugues_main.html'), name='portugues_main'),
    # path('english/',   lambda r: render(r, 'english_main.html'),   name='english_main'),
]

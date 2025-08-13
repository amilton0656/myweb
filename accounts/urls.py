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

]

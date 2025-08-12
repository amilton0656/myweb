from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("portugues/", include("portugues.urls")), 
    path("english/", include("english.urls")),
    path("", include("accounts.urls")),  # home e login/logout
]

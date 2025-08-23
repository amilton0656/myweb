from django.urls import path
from english import views

urlpatterns = [
    path('', views.english_main, name='english_main'),
    path('friends0101/', views.friends0101, name='friends0101'),
    path('friends0102/', views.friends0102, name='friends0102'),
    path('friends0103/', views.friends0103, name='friends0103'),
    path('friends0104/', views.friends0104, name='friends0104'),
    path('friends0105/', views.friends0105, name='friends0105'),
    path('friends0106/', views.friends0106, name='friends0106'),
    path('friends0107/', views.friends0107, name='friends0107'),
    path('friends0108/', views.friends0108, name='friends0108'),
    path('friends0109/', views.friends0109, name='friends0109'),

    path('friends0201/', views.friends0201, name='friends0201'),

    path('fun_vacations/', views.fun_vacations, name='fun_vacations'),
]
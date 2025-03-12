from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'), # URL para el inicio de sesión
    path('', views.home, name='home'),
]

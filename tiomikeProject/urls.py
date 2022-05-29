from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from tiomikeApp import views

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('usuario/', views.UserCreateView.as_view()),
    path('usuario/<int:pk>/', views.UserDetailView.as_view()),
    path('cliente/', views.ClienteCreateView.as_view()),
    path('cliente/<int:pk>/', views.ClienteDetailView.as_view()),
    path('rol/', views.RolCreateView.as_view()),
    path('rol/<int:pk>/', views.RolDetailView.as_view()),
    path('tamano/', views.TamanoCreateView.as_view()),
    path('tamano/<int:pk>/', views.TamanoDetailView.as_view()),
    path('cita/', views.CitaCreateView.as_view()),
    path('cita/<int:pk>/', views.CitaDetailView.as_view()),
    path('mascota/', views.MascotaCreateView.as_view()),
    path('mascota/<int:pk>/', views.MascotaDetailView.as_view()),
    path('tipoIdentificacion/', views.TipoIdentificacionCreateView.as_view()),
    path('tipoIdentificacion/<int:pk>/', views.TipoIdentificacionDetailView.as_view()),
    path('estado/', views.EstadoCreateView.as_view()),
    path('estado/<int:pk>/', views.EstadoDetailView.as_view()),
]
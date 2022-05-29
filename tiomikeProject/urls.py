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
]
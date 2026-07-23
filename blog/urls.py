"""URLs de la app blog."""
from django.urls import path
from . import views

urlpatterns = [
    # Página de inicio: http://localhost:8000/
    path('', views.index, name='index'),
    
    # Detalle de un post: http://localhost:8000/post/1/
    path('post/<int:pk>/', views.detail, name='detail'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('R2', views.graficar_vectorR2, name='vectorR2'),
    path('R3', views.vector_grafico, name='vectorR3'),
    path('grafico-3d/', views.grafico_vector, name='grafico_vector'),
    
]
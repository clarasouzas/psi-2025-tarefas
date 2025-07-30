from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sobre/', views.sobre, name='sobre'),
    path('postagens/', views.lista_postagens, name='lista_postagens'), 
    path('postagem/<int:pk>/', views.postagem_detalhe, name='postagem_detalhe'),
]

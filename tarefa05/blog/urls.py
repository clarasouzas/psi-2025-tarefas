from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sobre/', views.sobre, name='sobre'),
    path('posts/', views.lista_postagens, name='lista_postagens'),
    path('postagem/<int:id_post>/', views.postagem_detalhe, name='postagem_detalhe'),
]
from django.shortcuts import render, get_object_or_404
from .models import Postagem

def index(request):
    postagens = Postagem.objects.order_by('-data_publicacao')
    return render(request, 'blog/index.html', {'postagens': postagens})

def sobre(request):
    # Caso tenha conteúdo dinâmico, passe contexto aqui
    return render(request, 'blog/sobre.html')

def lista_postagens(request):
    postagens = Postagem.objects.order_by('-data_publicacao')
    return render(request, 'blog/posts.html', {'postagens': postagens})

def postagem_detalhe(request, pk):
    postagem = get_object_or_404(Postagem, pk=pk)
    return render(request, 'blog/postagem_detalhe.html', {'postagem': postagem})

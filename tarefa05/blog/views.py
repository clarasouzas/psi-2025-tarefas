from django.shortcuts import render, get_object_or_404
from .models import Postagem, Blog, ConteudoPagina

def index(request):
    context = {
        "postagens": Postagem.objects.order_by('-data_publicacao'),
        "blog": Blog.objects.first(),
        "conteudo": ConteudoPagina.objects.filter(pagina='inicio').first(),
    }
    return render(request, "blog/index.html", context)

def sobre(request):
    context = {
        "blog": Blog.objects.first(),
        "conteudo": ConteudoPagina.objects.filter(pagina='sobre').first(),
    }
    return render(request, "blog/sobre.html", context)

def lista_postagens(request):
    context = {
        "postagens": Postagem.objects.order_by('-data_publicacao'),
        "blog": Blog.objects.first(),
    }
    return render(request, "blog/posts.html", context)

def postagem_detalhe(request, id_post):
    postagem = get_object_or_404(Postagem,id = id_post)
    context = {
        "postagem": postagem,
        "blog": Blog.objects.first(),
    }
    return render(request, "blog/postagem_detalhe.html", context)

from django.shortcuts import render, get_object_or_404
from .models import Postagem, ConteudoSite

def index(request):
    postagens = Postagem.objects.order_by('-data_publicacao')
    conteudo = ConteudoSite.objects.filter(pagina='inicio').first()
    return render(request, 'blog/index.html', {
        'postagens': postagens,
        'conteudo': conteudo,
    })

def sobre(request):
    conteudo = ConteudoSite.objects.filter(pagina='sobre').first()
    return render(request, 'blog/sobre.html', {'conteudo': conteudo})

def lista_postagens(request):
    postagens = Postagem.objects.order_by('-data_publicacao')
    return render(request, 'blog/posts.html', {'postagens': postagens})

def postagem_detalhe(request, pk):
    postagem = get_object_or_404(Postagem, pk=pk)
    return render(request, 'blog/postagem_detalhe.html', {'postagem': postagem})



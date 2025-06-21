from django.shortcuts import render

def index(request):
    return render(request, "index.html")
def usuarios(request):
    usuarioslista = [
        {
        "Nome": "Lucas Andrade",
        "Matrícula": "20251001",
        "Idade": 22,
        "Cidade": "Belo Horizonte"
    },
    {
        "Nome": "Marina Costa",
        "Matrícula": "20251002",
        "Idade": 25,
        "Cidade": "São Paulo"
    },
    {
        "Nome": "João Pedro Lima",
        "Matrícula": "20251003",
        "Idade": 28,
        "Cidade": "Curitiba"
    },
    {
        "Nome": "Ana Beatriz Soares",
        "Matrícula": "20251004",
        "Idade": 20,
        "Cidade": "Salvador"
    },
    {
        "Nome": "Rafael Martins",
        "Matrícula": "20251005",
        "Idade": 23,
        "Cidade": "Porto Alegre"
    }
    ]
    context = {
        "usuarios": usuarioslista,
    }
    return render(request, "usuarios.html", context)

# Create your views here.

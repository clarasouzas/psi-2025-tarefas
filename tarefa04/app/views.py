from django.shortcuts import render

from .models import Tarefa
from django.utils import timezone

def lista_tarefas(request):
    tarefas = Tarefa.objects.all()
    hoje = timezone.now()
    context = {
        'tarefas': tarefas,
        'hoje': timezone.now(),
    }
    return render(request, 'app/lista.html', context)
from datetime import date
from django.shortcuts import render
from .models import Tarefa

def lista_tarefas(request):
    tarefas = Tarefa.objects.all()
    context = {
        'tarefas': tarefas,
        'hoje': date.today(),
    }
    return render(request, 'app/lista.html', context)
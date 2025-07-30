from django.db import models
from datetime import date


class Tarefa(models.Model):
    PENDENTE = 'Pendente'
    CONCLUIDA = 'Concluída'
    EM_ANDAMENTO = 'Em Andamento'

    STATUS_CHOICES = [
        (PENDENTE, 'Pendente'),
        (CONCLUIDA, 'Concluída'),
        (EM_ANDAMENTO, 'Em andamento'),
    ]

    nome = models.CharField('Título', max_length=100)
    status = models.CharField('Status', max_length=20, choices=STATUS_CHOICES, default=PENDENTE)
    prazo = models.DateField('Prazo')

    class Meta:
        ordering = ['-prazo']
      

    def __str__(self):
        return self.nome

    @property
    def atrasada(self):
        return self.prazo < date.today() and self.status != self.CONCLUIDA

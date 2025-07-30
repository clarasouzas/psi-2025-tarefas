from django.db import models
from django.utils import timezone

class Tarefa(models.Model):
    PENDENTE = 'Pendente'
    CONCLUIDA = 'Concluída'
    EM_ANDAMENTO = 'Em Andamento'

    STATUS = [
        (PENDENTE, 'Pendente'),
        (CONCLUIDA, 'Concluída'),
        (EM_ANDAMENTO, 'Em andamento'),
    ]

    nome = models.CharField('Título', max_length=100)
    status = models.CharField('Status', max_length=20, choices=STATUS, default=PENDENTE)
    prazo = models.DateTimeField('Prazo')

    class Meta:
        ordering = ['-prazo']
      

    def __str__(self):
        return self.nome

    @property
    def atrasada(self):
        hoje = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
        return self.prazo < hoje and self.status != self.CONCLUIDA
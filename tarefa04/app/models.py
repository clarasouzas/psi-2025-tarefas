from django.db import models
from datetime import date

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
    prazo = models.DateField('Prazo',null=False, blank=False)

    class Meta:
        ordering = ['-prazo']
      

    def __str__(self):
        return self.nome

    @property
    def atrasada(self):
        if self.prazo is None:
            return False
        return self.prazo < date.today() and self.status != self.CONCLUIDA
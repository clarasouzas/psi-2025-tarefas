from django.db import models
from datetime import datetime

class Postagem(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)
    imagem = models.ImageField(upload_to='postagens/', null=True, blank=True)

    def __str__(self):
        return self.titulo

class ConteudoSite(models.Model):
    PAGINAS = [
        ('sobre', 'Sobre'),
        ('header', 'Header'),
        ('inicio', 'Início'),
    ]

    pagina = models.CharField(max_length=20, choices=PAGINAS, unique=True)
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=300, blank=True)
    texto = models.TextField(blank=True)
    imagem_header = models.ImageField(upload_to='conteudo_site/', null=True, blank=True)

    
    def __str__(self):
        return f"Conteúdo da página {self.pagina}"

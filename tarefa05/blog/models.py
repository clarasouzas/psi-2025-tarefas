from django.db import models
from datetime import datetime

class Postagem(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)
    imagem = models.ImageField(upload_to='postagens/', null=True, blank=True)

    def __str__(self):
        return self.titulo
    
class ConteudoPagina(models.Model):
    PAGINAS = [
        ('inicio', 'Início'),
        ('sobre', 'Sobre'),
        
    ]
    pagina = models.CharField(max_length=20, choices=PAGINAS, unique=True)
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=300, blank=True)
    texto = models.TextField(blank=True)
    imagem_header = models.ImageField(upload_to='banner/', null=True, blank=True)

    def __str__(self):
        return self.pagina



class Blog(models.Model):
    titulo = models.CharField("Título do site", max_length=200)

    instagram = models.URLField("Instagram", blank=True)
    youtube = models.URLField("YouTube", blank=True)
    x = models.URLField("X (Twitter)", blank=True)
    facebook = models.URLField("Facebook", blank=True)
    linkedin = models.URLField("LinkedIn", blank=True)
    tiktok = models.URLField("TikTok", blank=True)

    copyright = models.CharField("Copyright", max_length=100, default="Seu Nome")
    ano = models.PositiveIntegerField("Ano", default=datetime.now().year)

    def __str__(self):
        return "Configurações do Site"
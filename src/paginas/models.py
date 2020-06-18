from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Paginas(models.Model):
    dono = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField('Titulo', max_length=200)
    conteudo = models.TextField('Conteudo')
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo
    """
    Implementando mais modelos de paginas...

    """
    

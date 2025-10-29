from django.db import models
from django.contrib.auth.models import AbstractUser
from .utils import STATUS_CHOICES

# Create your models here.
class Usuario(AbstractUser):
    nome = models.CharField(max_length=100, blank=False, null=False)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    
    def __str__(self):
        return self.nome
    
    
class Projeto(models.Model):
    titulo = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.CharField(max_length=100, null=False, blank=False)
    status = models.CharField(max_length=40)
    
    def __str__(self):
        return self.titulo
    
class Tarefa(models.Model):
    titulo = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.CharField(max_length=100, null=False, blank=False)
    responsavel = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='usuario_responsavel')
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name='projeto')
    
    def __str__(self) :
        return self.titulo


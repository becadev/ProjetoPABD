from .models import *
from rest_framework import serializers

class TarefaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarefa
        field = '__all__'
    
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        field = '__all__'
    
class ProjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projeto
        field = '__all__'
    
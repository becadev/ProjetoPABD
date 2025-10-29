from django.shortcuts import render
from .serializer import *
from .models import *
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

class LoginView(APIView):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()
    
    def get_queryset(self):
        return super().get_queryset()
    pass

class CadastroView(APIView):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()
    
    def get_queryset(self):
        return super().get_queryset()
    
    def post(self, request):
        pass
        
        
class Projetos(viewsets.ModelView):
    serializer_class = ProjetoSerializer
    queryset = Projeto.objects.all()
    
    def get_queryset(self):
        return super().get_queryset()
    
    @action(detail=True, methods=['post']) 
    def criar_tarefa(self, request):
        serializer = ProjetoSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        responsavel = serializer.validated_data['responsavel']
        titulo = serializer.validated_data['titulo']
        descricao = serializer.validated_data['descricao']
        projeto = serializer.validated_data['projeto']
        
        projeto = Projetos.objects.filter(id = projeto).first()
        
        if not projeto:
            return Response({"detail" : "Projeto não existe"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            Tarefa.objects.creat(
                titulo = titulo,
                descricao = descricao,
                responsavel = responsavel,
                projeto = projeto
            )
        except Tarefa.ValueError:
            return Response({"detail": "Não foi possível criar tarefa"},status=status.HTTP_404_NOT_FOUND)
        
        return Response({"detail": "Tarefa criada"},status=status.HTTP_201_CREATED)
        
    
            
            
        
    
        


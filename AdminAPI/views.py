from django.shortcuts import render
from rest_framework import generics, viewsets
from AdminAPI.models import Local, Aluno, Encarregadoeducacao, Professor, Disciplina
from AdminAPI.serializers import LocalSerializer, AlunoSerializer, EncarregadoeducacaoSerializer, DisciplinaSerializer, ProfessorSerializer
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions

# Create your views here.

class LocalList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    queryset = Local.objects.all()
    serializer_class = LocalSerializer

class LocalDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    queryset = Local.objects.all()
    serializer_class = LocalSerializer


class AlunoList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class AlunoDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


class EncarregadoDeEducacaoList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    queryset = Encarregadoeducacao.objects.all()
    serializer_class = EncarregadoeducacaoSerializer

class EncarregadoDeEducacaoDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    queryset = Encarregadoeducacao.objects.all()
    serializer_class = EncarregadoeducacaoSerializer


class ProfessorList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

class ProfessorDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer


class DisciplinaList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer

class DisciplinaDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer
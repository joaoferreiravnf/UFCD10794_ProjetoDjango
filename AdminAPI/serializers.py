from rest_framework import serializers
from AdminAPI.models import Local
from AdminAPI.models import Aluno
from AdminAPI.models import Professor
from AdminAPI.models import Alunoanoescolaridade
from AdminAPI.models import Alunolocal
from AdminAPI.models import Anoescolaridade
from AdminAPI.models import Anoletivo
from AdminAPI.models import Dia
from AdminAPI.models import Disciplina
from AdminAPI.models import Encarregadoeducacao
from AdminAPI.models import Faltaaluno
from AdminAPI.models import Ocorrenciaaluno
from AdminAPI.models import Tarefa
from AdminAPI.models import Tarefaaluno
from AdminAPI.models import Tarefaalunoficheiro
from AdminAPI.models import Tarefaficheiro
from AdminAPI.models import Turma
from AdminAPI.models import Turmaaluno
from AdminAPI.models import Turmadisciplina
from AdminAPI.models import Turmadisciplinatimetable
from AdminAPI.models import Utilizador

class LocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Local
        fields = ("__all__")

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Aluno
        fields=('__all__')
class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Professor
        fields=('__all__')
class AlunoanoescolaridadeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Alunoanoescolaridade
        fields=('__all__')
class AlunolocalSerializer(serializers.ModelSerializer):
    class Meta:
        model=Alunolocal
        fields=('__all__')
class AnoescolaridadeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Anoescolaridade
        fields=('__all__')
class AnoletivoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Anoletivo
        fields=('__all__')
class DiaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Dia
        fields=('__all__')
class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Disciplina
        fields=('__all__')
class EncarregadoeducacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Encarregadoeducacao
        fields=('__all__')
class FaltaalunoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Faltaaluno
        fields=('__all__')
class OcorrenciaalunoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Ocorrenciaaluno
        fields=('__all__')
class TarefaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tarefa
        fields=('__all__')
class TarefaalunoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tarefaaluno
        fields=('__all__')
class TarefaalunoficheiroSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tarefaalunoficheiro
        fields=('__all__')
class TarefaficheiroSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tarefaficheiro
        fields=('__all__')
class TurmaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Turma
        fields=('__all__')
class TurmaalunoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Turmaaluno
        fields=('__all__')
class TurmadisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Turmadisciplina
        fields=('__all__')
class TurmadisciplinatimetableSerializer(serializers.ModelSerializer):
    class Meta:
        model=Turmadisciplinatimetable
        fields=('__all__')
class UtilizadorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Utilizador
        fields=('__all__')
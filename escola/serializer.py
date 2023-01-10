from rest_framework import serializers
from escola.models import Aluno, Curso, Matricula
from escola.validators import *

class AlunoSerializerV1(serializers.ModelSerializer):

    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'cpf', 'data_nascimento', 'email', 'celular', 'foto']
        
    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf':"O CPF deve ser válido: XXX.XXX.XXX-XX" })
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome':"Não inclua números neste campo"})
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular':"O deve estar no fromato: (XX) XXXXX-XXXX"})
        return data

class AlunoSerializerV2(serializers.ModelSerializer):

    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'cpf', 'rg','data_nascimento', 'email', 'celular', 'foto']
        
    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf':"O CPF deve estar no formato: XXX.XXX.XXX-XX"})
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome':"Não inclua números neste campo"})
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular':"O deve estar no fromato: (XX) XXXXX-XXXX"})
        return data


class CursoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Curso
        fields = '__all__'
        


class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = '__all__'


class ListaMatriculasPorAlunoSerializer(serializers.ModelSerializer):
    #Pegando o nome do curso classe herdada
    curso = serializers.ReadOnlyField(source='curso.descricao')
    #Pegando o nome do periodo da classe herdada
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']
    def get_periodo(self, objeto):
        return objeto.get_periodo_display()


class ListaAlunosPorCursoSerializer(serializers.ModelSerializer):
    aluno = serializers.ReadOnlyField(source='aluno.nome')
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        fields = ['id', 'aluno', 'periodo']
    def get_periodo(self, objeto):
        return objeto.get_periodo_display()

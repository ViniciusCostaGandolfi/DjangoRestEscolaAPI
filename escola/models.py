from django.db import models


class Aluno(models.Model):
    nome = models.CharField(max_length=50, blank=False, null=False)
    cpf = models.CharField(max_length=14, blank=False, null=False, unique=True)
    rg = models.CharField(max_length=14, default="")
    email = models.EmailField(blank=False, null=False, unique=True)
    celular = models.CharField(max_length=15, blank=False, null=False)
    data_nascimento = models.DateField(blank=False, null=False)
    foto = models.ImageField(blank=True)

    def __str__(self) -> str:
        return self.nome


class Curso(models.Model):

    choices = [
        ['B', 'Básico'],
        ['I', 'Intermediário'],
        ['A', 'Avançado']
    ]

    codigo = models.CharField(max_length=10, blank=False, null=False)
    descricao = models.CharField(max_length=100, blank=False, null=False)
    nivel = models.CharField(max_length=1, choices=choices, null=False, default='B', blank=False)

    def __str__(self) -> str:
        return self.descricao


class Matricula(models.Model):
    choices = [
        ['M', 'Manha'],
        ['T', 'Tarde'],
        ['N', 'Noite']
    ]
    # Referencia as matriculas aos alunos, e se o aluno for deletado, deletar tambem suas matriculas
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE) 
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    periodo = models.CharField(max_length=1, choices=choices, default='M', blank=False, null=False) 
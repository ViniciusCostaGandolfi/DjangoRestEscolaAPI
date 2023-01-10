from django.contrib import admin
from escola.models import Aluno, Curso, Matricula



class AlunoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf', 'data_nascimento')
    list_display_links = ('id', 'nome', 'cpf')
    search_fields = ('id', 'nome', 'cpf')
    list_per_page = 20


class CursoAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo', 'descricao', 'nivel')
    list_display_links = ('id', 'codigo', 'descricao', 'nivel')
    search_fields = ('id', 'codigo', 'descricao', 'nivel')
    list_filter = ['nivel']
    list_per_page = 20


class MatriculaAdmin(admin.ModelAdmin):
    list_display = ['id', 'periodo', 'aluno', 'curso']
    list_display_links  = ['id', 'periodo', 'aluno', 'curso']
    search_fields  = ['id', 'periodo', 'aluno', 'curso']
    list_filter = ['periodo']
    list_per_page = 20


admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Matricula, MatriculaAdmin)
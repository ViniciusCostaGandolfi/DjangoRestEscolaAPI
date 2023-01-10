from rest_framework import viewsets, generics, filters
from escola.models import Aluno, Curso, Matricula
from escola.serializer import *
from django_filters.rest_framework import DjangoFilterBackend
from django.http import HttpResponse
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework import status
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.renderers import JSONRenderer
from rest_framework_xml.renderers import XMLRenderer
from rest_framework_yaml.renderers import YAMLRenderer


# em todas as classes, por default estão:
#     authentication_classes = [BasicAuthentication]
#     permission_classes = [IsAuthenticated, DjangoModelPermissions]



class AlunosViewSet(viewsets.ModelViewSet):
    """ Exibindo todos os alunos """

    # Trazendo todos os alunos
    queryset = Aluno.objects.all() 
    # Filtros e Pesquisa
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome', 'id']
    search_fields = ['nome', 'id']

    #renderer_classes = (JSONRenderer, XMLRenderer, YAMLRenderer)

    # em todas as classes, por default estão:
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated, DjangoModelPermissions]



    def get_serializer_class(self):
        if self.request.version == 'v2':
            return AlunoSerializerV2
        else:
            return AlunoSerializerV1

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            headers = self.get_success_headers(serializer.data)
            id = str(serializer.data['id'])
            response = Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
            response['Location'] = request.build_absolute_uri() + id

            return response


        


class CursosViewSet(viewsets.ModelViewSet):
    """ Exibindo todos os Cursos """
    queryset = Curso.objects.all() # Trazendo todos os Cursos
    serializer_class = CursoSerializer # Serialização dos Cursos
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['codigo', 'nivel']
    search_fields = ['codigo']


class MatriculaViewSet(viewsets.ModelViewSet):
    """Listando todas as matriculas"""
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['aluno', 'curso']
    search_fields = ['aluno', 'curso']


    @method_decorator(cache_page(60))
    def list(self, *args, **kwargs):
        return super().list(*args, **kwargs)


class ListaMatriculasPorAlunoView(generics.ListAPIView):
    """Listando matriculas por aluno"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset
    
    serializer_class = ListaMatriculasPorAlunoSerializer
    http_method_names = ['get']


class ListaAlunosPorCursoView(generics.ListAPIView):
    """Listando alunos por curso"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    
    serializer_class = ListaAlunosPorCursoSerializer
    http_method_names = ['get']

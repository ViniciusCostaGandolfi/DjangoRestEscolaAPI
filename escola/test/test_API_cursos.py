from rest_framework.test import APITestCase
from escola.models import Curso
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import get_user
from django.contrib.auth import authenticate

#from rest_framework.test import force_authenticate





class CursosTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_superuser(
        email='asdf@gmail.com',
        password='hiwa_asdf',
        username='smile as we go ahead'
        )
        #authenticate(username='smile as we go ahead', password='hiwa_asdf')
        self.client.force_authenticate(self.user)
        #self.client.login(username=self.user.username, password=self.user.password)
    
        self.list_url = reverse('Cursos-list')
        self.curso_teste_1 = Curso.objects.create(
            codigo='JB1',
            descricao='Curso de Java Básico',
            nivel='B'
        )

        self.curso_teste_2 = Curso.objects.create(
            codigo='JI1',
            descricao='Curso de Java Intermediário',
            nivel='I'
        )

    # def test_fail(self):
    #     self.fail('Teste falhou de propósito')


    def test_GET_para_listar_cursos(self):
        """Teste para verificar se a requisição GET retorna os cursos"""

        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_requisicao_post_para_criar_curso(self):
        """Teste para verificar a requisição POST para criar um curso"""
        data = {
            'codigo':'CTT3',
            'descricao':'Curso teste 3',
            'nivel':'A'
        }
        response = self.client.post(self.list_url, data=data, format='json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_delete_para_deletar_curso(self):
        """Teste para verificar a requisição DELETE não permitida para deletar um curso"""
        response = self.client.delete('/cursos/1/')
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_requisicao_put_para_atualizar_curso(self):
        """Teste para verificar a requisição PUT para atualizar um curso"""
        data = {
            'codigo':'CTT1',
            'descricao':'Curso teste 1 atualizado',
            'nivel':'I'
        }
        response = self.client.put('/cursos/1/', data=data, format='json')
        self.assertEquals(response.status_code, status.HTTP_200_OK)
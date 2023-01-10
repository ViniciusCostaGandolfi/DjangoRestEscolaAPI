from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status



class AutenticacaoUserTestCase(APITestCase):

    def setUp(self):

        self.user = User.objects.create_user('c3po', password='12345')
        self.list_url = reverse('Cursos-list')

    def test_autenticacao_com_credenciais_corretas(self):
        """Verifica autenticação de um usuário com credenciais corretas"""

        user = authenticate(username='c3po', password='12345')

        self.assertTrue((user is not None) and user.is_authenticated)


    def test_autenticacao_de_user_com_password_incorreto(self):
        """Teste que verifica autenticação de um user com password incorreto"""
        user = authenticate(username='c3po', password='123455')
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_requisicao_get_com_user_autenticado(self):
        """Teste que verifica uma requisição GET de um user autenticado"""
        self.client.force_authenticate(self.user)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


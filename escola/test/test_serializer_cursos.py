from django.test import TestCase
from escola.models import Curso
from escola.serializer import CursoSerializer


class ProgramaModelTestCase(TestCase):

    def setUp(self):
        self.curso_teste_1 = Curso(
            codigo='JB2',
            descricao='Curso de Java OO',
            nivel='B'
        )
        self.serializer = CursoSerializer(instance=self.curso_teste_1)


    def test_verifica_campos_serializados_curso(self):
        """Teste que verifica os campos que estão sendo serializados do curso"""

        data = self.serializer.data

        self.assertEqual(set(data.keys()), set(['id', 'codigo', 'descricao', 'nivel']))

    def test_verifica_campos_do_curso_serializados(self):
        """Teste que verifica os campos que estão sendo serializados do curso"""

        data = self.serializer.data

        self.assertEqual(data['codigo'], self.curso_teste_1.codigo)
        self.assertEqual(data['descricao'], self.curso_teste_1.descricao)
        self.assertEqual(data['nivel'], self.curso_teste_1.nivel)

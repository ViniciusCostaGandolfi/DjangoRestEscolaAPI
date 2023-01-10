from django.test import TestCase
from escola.models import Curso


class ProgramaModelTestCase(TestCase):

    def setUp(self):
        self.curso_teste_1 = Curso(
            codigo='JB2',
            descricao='Curso de Java OO',
            nivel='B'
        )

    def test_verifica_atributos_do_curso(self):
        """Teste que verifica os atributos do curso"""

        self.assertEqual(self.curso_teste_1.codigo, 'JB2')
        self.assertEqual(self.curso_teste_1.descricao, 'Curso de Java OO')
        self.assertEqual(self.curso_teste_1.nivel, 'B')


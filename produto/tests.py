from django.test import TestCase

from django.test import TestCase
import services 
from .models import Produto
#nome, peso_unitario, custo_por_quilo, diferencial, operacao_diferencial
class ProdutoServiceTests(TestCase):
    def test_criar_produto(self):
        produto = services.criar_produto('Bife', 10, 15, 5, '+')
        self.assertEqual(produto.nome, 'Bife')
        self.assertEqual(produto.peso_unitario, 10)
        self.assertEqual(produto.valor_total, 20)

    def test_atualizar_preco(self):
        produto = services.criar_produto('Camiseta', 49.90)
        produto = services.atualizar_preco(produto.id, 59.90)
        self.assertEqual(produto.preco, 59.90)


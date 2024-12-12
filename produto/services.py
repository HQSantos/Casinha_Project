from .models import Produto
from django.db import models

class ProdutoService:
    @staticmethod
    def criar_produto(nome, peso_unitario, custo_por_quilo, diferencial, operacao_diferencial):
        produto = Produto.objects.create(nome=nome, peso_unitario=peso_unitario, custo_por_quilo=custo_por_quilo,
        diferencial=diferencial, operacao_diferencial=operacao_diferencial,)
        Produto.calcular_diferencial(produto)
        return produto

    @staticmethod
    def atualizar_produto(produto_id, **dados):
        try:
            produto = Produto.objects.get(id=produto_id)
            for campo, valor in dados.items():
                setattr(produto, campo, valor)
            produto.save()
            return produto
        except Produto.DoesNotExist:
            raise ValueError(f"Produto com ID {produto_id} não encontrado.")
        
    @staticmethod
    def excluir_produto(produto_id):
        try:
            produto = Produto.objects.get(id=produto_id)
            produto.delete()
            return True
        except Produto.DoesNotExist:
            raise ValueError(f"Produto com ID {produto_id} não encontrado.")

    @staticmethod
    def listar_produtos():
        return Produto.objects.all()

    def filtrar_produtos(**kwargs):
        return Produto.objects.filter(**kwargs)
    #produtos = filtrar_produtos(estoque__gte=10)
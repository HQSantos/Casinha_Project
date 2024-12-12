from django.db import models
from .errors import ERROS
class Produto():
    def __init__(id, self, nome, peso_unitario, custo_por_quilo, valor_total, diferencial, operacao_diferencial):
        self._nome = nome 
        self._peso_unitario = peso_unitario
        self._custo_por_quilo = custo_por_quilo
        self._valor_total = valor_total
        self._diferencial = diferencial
        self._operacao_diferencial = operacao_diferencial

    @property
    def id(self):
        return self._id
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def set_nome(self, novo_nome):
        if len(novo_nome) == 0:
            raise ValueError(ERROS['NOME_VAZIO'])
        self._nome = novo_nome

    @property
    def peso_unitario(self):
        return self._peso_unitario

    @peso_unitario.setter
    def set_peso_unitario(self, novo_peso_unitario):
        if novo_peso_unitario <= 0:
            raise ValueError(ERROS['PESO_VAZIO'])
        self._peso_unitario = novo_peso_unitario

    @property
    def custo_por_quilo(self):
        return self._custo_por_quilo

    @custo_por_quilo.setter
    def set_custo_por_quilo(self, novo_custo_por_quilo):
        if novo_custo_por_quilo <= 0:
            raise ValueError(ERROS['CUSTO_VAZIO'])
        self._custo_por_quilo = novo_custo_por_quilo

    @property
    def valor_total(self):
        return self._valor_total

    @valor_total.setter
    def set_valor_total(self, novo_valor_total):
        if novo_valor_total < 0:
            raise ValueError(ERROS['TOTAL_VAZIO'])
        self._valor_total = novo_valor_total

    @property
    def diferencial(self):
        return self._diferencial

    @diferencial.setter
    def set_diferencial(self, novo_diferencial):
        if novo_diferencial < 0:
            raise ValueError(ERROS['OPERACAO_NEGATIVA'])
        self._diferencial = novo_diferencial
    
    @property
    def operacao_diferencial(self):
        return self._operacao_diferencial

    @operacao_diferencial.setter
    def set_operacao_diferencial(self, novo_operacao_diferencial):
        if novo_operacao_diferencial not in ('*', '+', '-', '/') :
            raise ValueError(ERROS['OPERACAO_ERRADA'])
        self._operacao_diferencial = novo_operacao_diferencial

    def calcular_diferencial(self):
        self._valor_total = eval(f"{self._custo_por_quilo} {self._operacao_diferencial} {self.diferencial}", {}, {"self": self})
        

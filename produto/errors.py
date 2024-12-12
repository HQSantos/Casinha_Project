from gettext import gettext as _

ERROS = {
    "NOME_VAZIO": _("Nome não pode ser vazio."),
    "PESO_VAZIO": _("Peso não pode ser negativo ou zero."),
    "CUSTO_VAZIO": _("Custo não pode ser negativo ou zero."),
    "TOTAL_VAZIO": _("Valor total não pode ser negativo ou zero."),
    "OPERACAO_NEGATIVA": _("Diferencial não pode ser negativo."),
    "OPERACAO_ERRADA": _("Operação incorreta, use apenas +,-,* ou /."),    
    'NAO_ENCONTRADO': ("Produto não encontrado."),
    'JA_EXISTE': ("Já existe um produto com esse nome."),
    'FILTRO_INVALIDO': ("Filtros inválidos."),
}
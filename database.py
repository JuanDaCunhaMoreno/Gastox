despesas = []
def adicionar_despesa(despesas):
    despesas.append(despesas)

def listar_despesas():
    return despesas

def remover_despesas():
    for despesa in despesas:
        if despesa.id == id:
            despesas.remove(despesa)
            return True #Sucesso
        return False #Não encontrou

def editar_despesa(id, novo_valor= None, nova_descricao= None, nova_data= None, nova_categoria= None):
    for despesa in despesas:
        if despesa.id == id:
            if novo_valor is not None:
                despesa.valor = novo_valor
            if nova_descricao is not None:
                despesa.descricao = nova_descricao
            if nova_data is not None:
                despesa.data = nova_data
            if nova_categoria is not None:
                despesa.categoria = nova_categoria
            return True #Sucesso
        return False #Não encontrou
    
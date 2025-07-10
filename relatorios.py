#Estatísticas e totais
def tot_categoria(lista_despesas):
    totais = {}
    for despesa in lista_despesas:
        categoria = despesa.categoria
        if categoria not in totais:
            totais[categoria] = 0
        totais[categoria] += despesa.valor
    return totais

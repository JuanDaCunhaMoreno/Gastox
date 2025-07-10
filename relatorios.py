#Estatísticas e totais
def tot_categoria(lista_despesas):
    totais = {}
    for despesa in lista_despesas:
        categoria = despesa.categoria
        if categoria not in totais:
            totais[categoria] = 0
        totais[categoria] += despesa.valor
    return totais


def estat_gerais(lista_despesas):
    if not lista_despesas:
        return None #Sem despesa
    
    total = sum(d.valor for d in lista_despesas)
    quantidade = len(lista_despesas)
    media = total / quantidade
    maior = max(lista_despesas, key=lambda d: d.valor)
    menor = min(lista_despesas, key=lambda d: d.valor)

    return {
        "total": total,
        "quantidade": quantidade,
        "media": media,
        "maior": maior,
        "menor": menor
    }

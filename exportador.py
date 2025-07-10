#Exportador
import csv

def exportar_despesas(lista_despesas, nome_arquivo="Despesas_exportadas.csv"):
    with open(nome_arquivo, mode="w", newline="", encoding="utf-8") as arquivo_csv:
        writer = csv.writer(arquivo_csv)

#Cabeçalho CSV
        writer.writerow(["ID", "Valor", "Descrição", "Data", "Categoria"])
#Linhas com os dados
        for despesa in lista_despesas:
            writer.writerow([
                despesa.id,
                f"{despesa.valor:.2f}",
                despesa.descricao,
                despesa.data,
                despesa.categoria
            ])

    return nome_arquivo #Retorna o nome do arquivo gerado

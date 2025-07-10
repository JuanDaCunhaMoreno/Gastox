from relatorios import tot_categoria, estat_gerais
from models import Despesa
from database import adicionar_despesa, listar_despesas, remover_despesas, editar_despesa
from time import sleep
from exportador import exportar_despesas

def exibir_menu():
    print("\n1 - Cadastrar gasto")
    print("2 - Editar gasto")
    print("3 - Remover gasto")
    print("4 - Listar gastos")
    print("5 - Exibir total por categoria")
    print("6 - Estatísticas gerais")
    print("7 - Exportar dados")
    print("0 - Sair")

def executar():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            id = input("ID: ")
            valor = float(input("Valor: "))
            descricao = input("Descrição: ")
            data = input("Data: ")
            categoria = input("Categoria: ")
            nova_despesa = Despesa(id, valor, descricao, data, categoria)
            adicionar_despesa(nova_despesa)
            print("Gasto adicionado!")

        elif opcao == '2':
            editar_id = input("Digite o ID para editar!")
            print("Deixe em branco para manter mesmo valor!")

            novo_valor = input("Novo valor: ")
            novo_valor = float(novo_valor) if novo_valor else None
            nova_descricao = input("Nova descrição: ") or None
            nova_data = input("Nova data (dd/mm/aaaa): ") or None
            nova_categoria = input("Nova categoria: ") or None

            sucesso = editar_despesa(editar_id, novo_valor, nova_descricao, nova_data, nova_categoria)

            if sucesso:
                print("Despesa editada com sucesso!")
            else:
                print("Despesa não encontrada!")

        elif opcao == '3':
            removerID = input("Digite o ID para ser removido: ")
            if remover_despesas(removerID):
                print("Despesa removida com sucesso!")
            else:
                print("Despesa não encontrada!")

        elif opcao == '4':
            for despesa in listar_despesas():
                print(despesa)

        elif opcao == '5':
            totais = tot_categoria(listar_despesas())
            print("\nTotal de gastos por categoria: ")
            for categoria, total in totais.items():
                print(f"{categoria}: R$ {total:.2f}")

        elif opcao == '6':
            estat = estat_gerais(listar_despesas())

            if estat is None:
                print("Nenhuma despesa registrada.")
            else:
                print("\n Estatísticas Gerais:")
                print(f"Total de gastos R$ {estat['total']:.2f}")
                print(f"Quantidade de despesas: {estat['quantidade']}")
                print(f"Média por despesa: R$ {estat['media']:.2f}")
                print(f"Maior gasto: {estat['maior'].valor:.2f} ({estat['maior'].descricao})")
                print(f"Menor gasto: {estat['menor'].valor:.2f} ({estat['menor'].descricao})")

        elif opcao == '7':
            nome_arquivo = exportar_despesas(listar_despesas())
            print(f"Despesas exportadas com sucesso para o arquivo: {nome_arquivo}")

        elif opcao == '0':
            print("Saindo...")
            sleep(0.5)
            break

if __name__ == "__main__":
    executar()

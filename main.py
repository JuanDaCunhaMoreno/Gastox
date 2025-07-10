from relatorios import tot_categoria
from models import Despesa
from database import adicionar_despesa, listar_despesas, remover_despesas, editar_despesa
from time import sleep

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
            editar_id = input("Digite o ID para editira!")
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

        elif opcao == '0':
            print("Saindo...")
            sleep(0.5)
            break

if __name__ == "__main__":
    executar()

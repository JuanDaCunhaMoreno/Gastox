from models import Despesa
from database import adicionar_despesa, listar_despesas, remover_despesas
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

        elif opcao == '3':
            removerID = input("Digite o ID para ser removido: ")
            if remover_despesas(removerID):
                print("Despesa removida com sucesso!")
            else:
                print("Despesa não encontrada!")

        elif opcao == '4':
            for despesa in listar_despesas():
                print(despesa)
        elif opcao == '0':
            print("Saindo...")
            sleep(0.5)
            break

if __name__ == "__main__":
    executar()

from controller import usuario_controller


def tela_inserir_produto():
    print("=== INSERIR PRODUTO ===")
    nome = input("Nome do produto: ")

    try:
        quantidade = int(input("Quantidade inicial em estoque: "))
    except ValueError:
        print("Quantidade inválida. Digite apenas números.")
        print()
        return

    sucesso, mensagem = usuario_controller.controlador_inserir_produto(nome, quantidade)
    print(mensagem)
    print()
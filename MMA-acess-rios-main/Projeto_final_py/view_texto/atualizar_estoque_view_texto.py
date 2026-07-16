# ============================================================
# ARQUIVO: view/atualizar_estoque_view_texto.py
# ============================================================
# Camada VIEW (Visão) - Atualizar Estoque em modo TEXTO (terminal)
# ============================================================

from controller import usuario_controller


def tela_atualizar_estoque():
    """
    Exibe a tela de atualização (reposição) de estoque: soma
    uma quantidade ao estoque atual do produto.
    """
    print("=== ATUALIZAR ESTOQUE ===")
    nome = input("Nome do produto: ")

    try:
        quantidade = int(input("Quantidade a adicionar ao estoque: "))
    except ValueError:
        print("Quantidade inválida. Digite apenas números.")
        print()
        return

    sucesso, mensagem = usuario_controller.controlador_atualizar_estoque(nome, quantidade)
    print(mensagem)
    print()
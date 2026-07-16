# ============================================================
# ARQUIVO: view/comprar_view_texto.py
# ============================================================
# Camada VIEW (Visão) - Registrar Compra em modo TEXTO (terminal)
# ============================================================

from controller import usuario_controller


def tela_registrar_compra():
    """
    Exibe a tela de registro de compra: abate do estoque e
    grava no histórico de compras.
    """
    print("=== REGISTRAR COMPRA ===")
    nome = input("Nome do produto: ")

    try:
        quantidade = int(input("Quantidade comprada: "))
    except ValueError:
        print("Quantidade inválida. Digite apenas números.")
        print()
        return

    sucesso, mensagem = usuario_controller.controlador_registrar_compra(nome, quantidade)
    print(mensagem)
    print()
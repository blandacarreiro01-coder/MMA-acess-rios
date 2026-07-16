# ============================================================
# ARQUIVO: view/pesquisar_view_texto.py
# ============================================================
# Camada VIEW (Visão) - Pesquisar Produto em modo TEXTO (terminal)
# ============================================================

from controller import usuario_controller


def tela_pesquisar_produto():
    """
    Exibe a tela de pesquisa de produto pelo nome, no terminal.
    """
    print("=== PESQUISAR PRODUTO ===")
    nome = input("Nome do produto a pesquisar: ")

    encontrado, mensagem = usuario_controller.controlador_pesquisar_produto(nome)
    print(mensagem)
    print()

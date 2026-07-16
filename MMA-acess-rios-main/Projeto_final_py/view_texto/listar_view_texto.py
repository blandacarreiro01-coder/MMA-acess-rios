# ============================================================
# ARQUIVO: view/listar_view_texto.py
# ============================================================
# Camada VIEW (Visão) - Listar Usuários em modo TEXTO (terminal)
# ============================================================

from controller import usuario_controller


def tela_listar_produtos():
    """
    Exibe no terminal a lista de todos os produtos cadastrados.
    """
    print("=== LISTA DE PRODUTOS ===")
    produtos = usuario_controller.controlador_listar_produtos()

    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
    else:
        for produto in produtos:
            print("-", produto)

    print()

# ============================================================
# ARQUIVO: view/pesquisar_view_texto.py
# ============================================================
# Camada VIEW (Visão) - Pesquisar Usuário em modo TEXTO (terminal)
# ============================================================

from controller import usuario_controller


def tela_pesquisar_texto():
    """
    Exibe a tela de pesquisa de usuário pelo login, no terminal.
    """
    print("=== PESQUISAR USUÁRIO ===")
    login = input("Login a pesquisar: ")

    encontrado, mensagem = usuario_controller.controlador_pesquisar_usuario(login)
    print(mensagem)
    print()

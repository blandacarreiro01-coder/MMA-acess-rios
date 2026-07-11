# ============================================================
# ARQUIVO: view/remover_view_texto.py
# ============================================================
# Camada VIEW (Visão) - Remover Usuário em modo TEXTO (terminal)
# ============================================================

from controller import usuario_controller


def tela_remover_texto():
    """
    Exibe a tela de remoção de usuário pelo login, no terminal.
    """
    print("=== REMOVER USUÁRIO ===")
    login = input("Login a remover: ")

    sucesso, mensagem = usuario_controller.controlador_remover_usuario(login)
    print(mensagem)
    print()

# ============================================================
# ARQUIVO: view/listar_view_texto.py
# ============================================================
# Camada VIEW (Visão) - Listar Usuários em modo TEXTO (terminal)
# ============================================================

from controller import usuario_controller


def tela_listar_texto():
    """
    Exibe no terminal a lista de todos os logins cadastrados.
    Não exibe as senhas.
    """
    print("=== LISTA DE USUÁRIOS ===")
    logins = usuario_controller.controlador_listar_usuarios()

    if len(logins) == 0:
        print("Nenhum usuário cadastrado.")
    else:
        for login in logins:
            print("-", login)

    print()

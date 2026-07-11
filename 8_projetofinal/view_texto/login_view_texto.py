# ============================================================
# ARQUIVO: view/login_view_texto.py
# ============================================================
# Camada VIEW (Visão) - Tela de Login em modo TEXTO (terminal)
#
# Repare que ela importa o MESMO controller usado pela versão
# Streamlit (controller/usuario_controller.py). Isso mostra que
# a regra de negócio (Controller) e os dados (Model) não sabem
# e não precisam saber qual interface está sendo usada.
# ============================================================

from controller import usuario_controller


def tela_login_texto():
    """
    Exibe a tela de login no terminal.

    Retorna uma tupla (autenticado, login):
        autenticado -> True se o login deu certo, False caso contrário
        login       -> o login digitado, caso tenha dado certo
    """
    print("=== LOGIN ===")
    login = input("Login: ")
    senha = input("Senha: ")

    # A tela só pergunta ao Controller se está tudo certo.
    # Ela não sabe (e não precisa saber) como essa verificação é feita.
    if usuario_controller.controlador_login(login, senha):
        print(f"Login realizado com sucesso! Bem-vindo, {login}.\n")
        return True, login
    else:
        print("Login ou senha incorretos. Tente novamente.\n")
        return False, ""

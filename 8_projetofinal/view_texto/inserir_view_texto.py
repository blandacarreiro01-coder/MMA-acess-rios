# ============================================================
# ARQUIVO: view/inserir_view_texto.py
# ============================================================
# Camada VIEW (Visão) - Inserir Usuário em modo TEXTO (terminal)
#
# Repare que o Controller chamado aqui (controlador_inserir_usuario)
# é EXATAMENTE o mesmo usado na tela Streamlit (view/inserir_view.py).
# Só muda a forma de coletar os dados (input() em vez de st.text_input()).
# ============================================================

from controller import usuario_controller


def tela_inserir_texto():
    """
    Exibe a tela de cadastro de um novo usuário no terminal.
    """
    print("=== INSERIR USUÁRIO ===")
    login = input("Novo login: ")
    senha = input("Nova senha: ")

    sucesso, mensagem = usuario_controller.controlador_inserir_usuario(login, senha)
    print(mensagem)
    print()

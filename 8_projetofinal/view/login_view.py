# ============================================================
# ARQUIVO: view/login_view.py
# ============================================================
# Camada VIEW (Visão) - Tela de Login
#
# Responsabilidade desta tela: apenas exibir os campos de login
# e senha, coletar o que o usuário digitou e chamar o Controller.
#
# Esta tela NUNCA acessa o dicionário de usuários diretamente.
# ============================================================

import streamlit as st
from controller import usuario_controller


def tela_login():
    """
    Exibe a tela inicial de login do sistema.
    """
    st.title("🔐 Sistema de Cadastro de Usuários")
    st.header("Login")

    # Campos para o usuário digitar o login e a senha
    login = st.text_input("Login")
    senha = st.text_input("Senha", type="password")

    # Botão para tentar entrar no sistema
    if st.button("Entrar"):
        # A tela apenas pergunta ao Controller se as credenciais
        # estão corretas. Ela não sabe (e não precisa saber) como
        # essa verificação é feita.
        login_valido = usuario_controller.controlador_login(login, senha)

        if login_valido:
            # Guarda na sessão que o usuário está autenticado,
            # para que o sistema "lembre" disso entre as telas.
            st.session_state.autenticado = True
            st.session_state.usuario_logado = login
            st.session_state.tela = "menu"
            st.rerun()
        else:
            st.error("Login ou senha incorretos.")

    st.info("Dica: o usuário administrador padrão é login **admin** e senha **123**.")

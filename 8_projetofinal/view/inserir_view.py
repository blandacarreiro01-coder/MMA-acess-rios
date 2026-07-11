# ============================================================
# ARQUIVO: view/inserir_view.py
# ============================================================
# Camada VIEW (Visão) - Inserir Usuário
#
# Esta tela apenas coleta o login e a senha do novo usuário e
# repassa esses dados para o Controller, que decide se pode ou
# não cadastrar.
# ============================================================

import streamlit as st
from controller import usuario_controller


def tela_inserir():
    """
    Exibe a tela de cadastro (inserção) de um novo usuário.
    """
    st.title("➕ Inserir Usuário")

    login = st.text_input("Novo login")
    senha = st.text_input("Nova senha", type="password")

    if st.button("Cadastrar"):
        sucesso, mensagem = usuario_controller.controlador_inserir_usuario(login, senha)

        if sucesso:
            st.success(mensagem)
        else:
            st.error(mensagem)

    st.write("---")

    # Botão para voltar ao menu principal
    if st.button("⬅ Voltar ao menu"):
        st.session_state.tela = "menu"
        st.rerun()

# ============================================================
# ARQUIVO: view/remover_view.py
# ============================================================
# Camada VIEW (Visão) - Remover Usuário
#
# Esta tela coleta o login do usuário a ser removido e repassa
# para o Controller, que aplica as regras de negócio (por
# exemplo, não deixar remover o usuário "admin").
# ============================================================

import streamlit as st
from controller import usuario_controller


def tela_remover():
    """
    Exibe a tela de remoção de usuário pelo login.
    """
    st.title("🗑️ Remover Usuário")

    login = st.text_input("Login a remover")

    if st.button("Remover"):
        sucesso, mensagem = usuario_controller.controlador_remover_usuario(login)

        if sucesso:
            st.success(mensagem)
        else:
            st.warning(mensagem)

    st.write("---")

    if st.button("⬅ Voltar ao menu"):
        st.session_state.tela = "menu"
        st.rerun()

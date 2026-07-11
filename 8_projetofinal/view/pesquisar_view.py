# ============================================================
# ARQUIVO: view/pesquisar_view.py
# ============================================================
# Camada VIEW (Visão) - Pesquisar Usuário
#
# Esta tela coleta o login que se deseja pesquisar e mostra o
# resultado devolvido pelo Controller. Nunca exibe a senha.
# ============================================================

import streamlit as st
from controller import usuario_controller


def tela_pesquisar():
    """
    Exibe a tela de pesquisa de usuário pelo login.
    """
    st.title("🔎 Pesquisar Usuário")

    login = st.text_input("Login a pesquisar")

    if st.button("Pesquisar"):
        encontrado, mensagem = usuario_controller.controlador_pesquisar_usuario(login)

        if encontrado:
            st.success(mensagem)
        else:
            st.warning(mensagem)

    st.write("---")

    if st.button("⬅ Voltar ao menu"):
        st.session_state.tela = "menu"
        st.rerun()

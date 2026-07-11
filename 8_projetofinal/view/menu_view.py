# ============================================================
# ARQUIVO: view/menu_view.py
# ============================================================
# Camada VIEW (Visão) - Menu Principal
#
# Exibe as opções do sistema depois que o usuário faz login com
# sucesso. Cada botão apenas troca a tela atual (guardada em
# st.session_state.tela) e chama st.rerun() para recarregar a
# página mostrando a nova tela.
# ============================================================

import streamlit as st


def tela_menu():
    """
    Exibe o menu principal com as opções do sistema.
    """
    st.title("📋 Menu Principal")
    st.write(f"Usuário logado: **{st.session_state.usuario_logado}**")

    st.header("Escolha uma opção")

    if st.button("1️⃣ Inserir usuário"):
        st.session_state.tela = "inserir"
        st.rerun()

    if st.button("2️⃣ Pesquisar usuário"):
        st.session_state.tela = "pesquisar"
        st.rerun()

    if st.button("3️⃣ Remover usuário"):
        st.session_state.tela = "remover"
        st.rerun()

    if st.button("4️⃣ Listar todos os usuários"):
        st.session_state.tela = "listar"
        st.rerun()

    if st.button("5️⃣ Logout"):
        # Limpa os dados da sessão e volta para a tela de login
        st.session_state.autenticado = False
        st.session_state.usuario_logado = ""
        st.session_state.tela = "login"
        st.rerun()

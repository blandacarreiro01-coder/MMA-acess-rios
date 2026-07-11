# ============================================================
# ARQUIVO: view/listar_view.py
# ============================================================
# Camada VIEW (Visão) - Listar Usuários
#
# Exibe todos os logins cadastrados no sistema, sem exibir as
# senhas, conforme exigido no enunciado do trabalho.
# ============================================================

import streamlit as st
from controller import usuario_controller


def tela_listar():
    """
    Exibe a tela com a lista de todos os logins cadastrados.
    """
    st.title("📄 Lista de Usuários")

    logins = usuario_controller.controlador_listar_usuarios()

    if len(logins) == 0:
        st.warning("Nenhum usuário cadastrado.")
    else:
        # Monta uma lista de dicionários apenas para exibir
        # de forma organizada em uma tabela (sem mostrar senha).
        dados_para_tabela = []
        for login in logins:
            dados_para_tabela.append({"Login": login})

        st.table(dados_para_tabela)

    st.write("---")

    if st.button("⬅ Voltar ao menu"):
        st.session_state.tela = "menu"
        st.rerun()

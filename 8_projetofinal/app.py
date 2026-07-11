# ============================================================
# ARQUIVO: app.py
# ============================================================
# Este é o arquivo PRINCIPAL do sistema. É ele que deve ser
# executado com o comando:
#
#     streamlit run app.py
#
# Caso ainda não tenha instalado o Streamlit, vá no terminal e
# execute: 
# 
#     pip install streamlit
#
# Responsabilidade deste arquivo:
#   1) Configurar a página do Streamlit.
#   2) Iniciar as variáveis de controle da sessão (session_state).
#   3) Fazer o "roteamento": decidir qual tela (View) deve ser
#      mostrada em cada momento, com base em
#      st.session_state.tela.
#
# A navegação entre as telas é feita através do session_state,
# que é uma espécie de "memória" que o Streamlit mantém durante
# toda a sessão do usuário no navegador.
# ============================================================

import streamlit as st

# Importa as funções de cada tela (camada View)
from view.login_view import tela_login
from view.menu_view import tela_menu
from view.inserir_view import tela_inserir
from view.pesquisar_view import tela_pesquisar
from view.remover_view import tela_remover
from view.listar_view import tela_listar


# Configuração básica da página
st.set_page_config(page_title="Cadastro de Usuários", page_icon="🔐")


# ------------------------------------------------------------
# Inicialização das variáveis de sessão
# ------------------------------------------------------------
# Essas variáveis só são criadas UMA VEZ, na primeira vez que o
# sistema é carregado. Nas próximas execuções (reruns), o
# Streamlit já vai encontrar esses valores prontos.

if "autenticado" not in st.session_state:
    # Indica se o usuário já fez login com sucesso
    st.session_state.autenticado = False

if "usuario_logado" not in st.session_state:
    # Guarda o login do usuário que está usando o sistema
    st.session_state.usuario_logado = ""

if "tela" not in st.session_state:
    # Guarda o nome da tela que deve ser exibida no momento
    st.session_state.tela = "login"


# ------------------------------------------------------------
# Roteamento das telas
# ------------------------------------------------------------
# Se o usuário ainda não estiver autenticado, o sistema sempre
# mostra a tela de login, não importa o que esteja em
# st.session_state.tela.

if not st.session_state.autenticado:
    tela_login()
else:
    # Usuário autenticado: escolhe a tela conforme o menu
    if st.session_state.tela == "menu":
        tela_menu()
    elif st.session_state.tela == "inserir":
        tela_inserir()
    elif st.session_state.tela == "pesquisar":
        tela_pesquisar()
    elif st.session_state.tela == "remover":
        tela_remover()
    elif st.session_state.tela == "listar":
        tela_listar()
    else:
        # Caso algo dê errado, volta para o menu por segurança
        st.session_state.tela = "menu"
        tela_menu()

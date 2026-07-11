# ============================================================
# ARQUIVO: view/menu_view_texto.py
# ============================================================
# Camada VIEW (Visão) - Menu Principal em modo TEXTO (terminal)
#
# Mostra as opções do sistema e devolve a opção escolhida pelo
# usuário. Não faz nenhuma regra de negócio, apenas exibe o menu.
# ============================================================


def tela_menu_texto(usuario_logado):
    """
    Exibe o menu principal no terminal e retorna a opção escolhida.
    """
    print("=== MENU PRINCIPAL ===")
    print(f"Usuário logado: {usuario_logado}")
    print("1 - Inserir usuário")
    print("2 - Pesquisar usuário")
    print("3 - Remover usuário")
    print("4 - Listar todos os usuários")
    print("5 - Logout")
    print("6 - Encerrar")

    opcao = input("Escolha uma opção: ")
    print()  # linha em branco para organizar a saída
    return opcao

# ============================================================
# ARQUIVO: app_texto.py
# ============================================================
# Este é o arquivo PRINCIPAL da versão em modo TEXTO (terminal)
# do sistema.
#
# IMPORTANTE PARA OS ALUNOS:
# Este arquivo usa o MESMO Model (model/) e o MESMO Controller
# (controller/) da versão em Streamlit (app.py). A única coisa
# que muda é a View: em vez de telas gráficas no navegador,
# usamos input() e print() no terminal.
#
# Isso mostra na prática a vantagem do padrão MVC: como a regra
# de negócio (Controller) e os dados (Model) não conhecem
# detalhes de interface, conseguimos "trocar" a tela inteira
# sem mexer em uma linha sequer do Model ou do Controller.
# ============================================================

from view_texto.login_view_texto import tela_login_texto
from view_texto.menu_view_texto import tela_menu_texto
from view_texto.inserir_view_texto import tela_inserir_produto
from view_texto.pesquisar_view_texto import tela_pesquisar_produto
from view_texto.remover_view_texto import tela_remover_produto
from view_texto.listar_view_texto import tela_listar_produtos

"""
Função que exibe o cabeçalho do programa.
Usada a cada vez que chamamos uma tela a partir do menu
"""
def exibir_cabecalho():
    print("\033c", end="")  # Limpa a tela do terminal
    print("-"*30)
    print("   SISTEMA LOJA MMACESSÓRIOS")
    print("-"*30)


def main():
    """
    Função principal: controla o fluxo do programa no terminal.
    Usamos um laço de repetição comum (while) para
    manter o programa rodando até o usuário escolher 'encerrar' no menu.
    """

    # Variáveis que guardam a situação do login e o usuário logado.
    autenticado = False
    usuario_logado = ""
    
    while True:
        exibir_cabecalho()

        if not autenticado:
            autenticado, usuario_logado = tela_login_texto()
            input("ENTER para continuar...")
            """
            Usando 'continue' para reiniciar o loop a partir desde ponto.
            Isso impede que o menu apareça caso o login não tenha dado certo.
            Assim, só sai do login quando o usuário loga corretamente.
            """
            continue
    
        opcao = tela_menu_texto(usuario_logado)

        if opcao == "1":
            exibir_cabecalho()
            tela_inserir_produto()

        elif opcao == "2":
            exibir_cabecalho()
            tela_pesquisar_produto()

        elif opcao == "3":
            exibir_cabecalho()
            tela_remover_produto()

        elif opcao == "4":
            exibir_cabecalho()
            tela_listar_produtos()

        elif opcao == "5":
            print("Programa fechado. Até logo!\n")
            break

        else:
            print("Opção inválida. Digite um número de 1 a 5.\n")

        input("ENTER para continuar...")


# Só executa a função main() quando o arquivo for rodado diretamente
# (e não quando for apenas importado por outro arquivo)
""" if __name__ == "__main__": """
main()

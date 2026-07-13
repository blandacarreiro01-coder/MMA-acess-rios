# ============================================================
# ARQUIVO: view/remover_view_texto.py
# ============================================================
# Camada VIEW (Visão) - Dar baixa em Produto em modo TEXTO (terminal)
# ============================================================

from controller import usuario_controller


def tela_remover_produto():
    print("=== DAR BAIXA EM PRODUTO ===")
    nome = input("Nome do produto: ")

    try:
        quantidade = int(input("Quantidade a dar baixa: "))
    except ValueError:
        print("Quantidade inválida. Digite apenas números.")
        print()
        return

    confirmacao = input(
        f"Confirma a baixa de {quantidade} unidade(s) de '{nome}'? (s/n): "
    ).strip().lower()

    if confirmacao != "s":
        print("Operação cancelada.")
        print()
        return

    sucesso, mensagem = usuario_controller.controlador_dar_baixa_produto(nome, quantidade)
    print(mensagem)
    print()
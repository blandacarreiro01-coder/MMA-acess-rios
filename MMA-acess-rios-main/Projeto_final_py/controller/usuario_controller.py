# ============================================================
# ARQUIVO: controller/usuario_controller.py
# ============================================================
# Camada CONTROLLER (Controlador)
# ============================================================

from model import usuario_model


def controlador_login(login, senha):
    return usuario_model.validar_login(login, senha)


def controlador_inserir_produto(nome, quantidade):
    """
    Regra de negócio para inserir um novo produto.

    Regras aplicadas:
        1) Nome não pode estar em branco.
        2) Quantidade não pode ser negativa.
        3) Não pode existir dois produtos com o mesmo nome.

    Retorna uma tupla (sucesso, mensagem).
    """
    nome = nome.strip()

    if nome == "":
        return False, "O nome do produto não pode ficar em branco."

    if quantidade < 0:
        return False, "A quantidade não pode ser negativa."

    if usuario_model.pesquisar_produto(nome):
        return False, f"O produto '{nome}' já está cadastrado."

    id_produto = usuario_model.inserir_produto(nome, quantidade)
    return True, f"Produto '{nome}' cadastrado com sucesso! ID gerado: {id_produto}"


def controlador_dar_baixa_produto(nome, quantidade_baixa):
    """
    Regra de negócio para dar baixa em uma quantidade de um produto.

    Regras aplicadas:
        1) Quantidade a dar baixa precisa ser maior que zero.
        2) Produto precisa existir.
        3) Quantidade a dar baixa não pode ser maior que o estoque atual.

    Retorna uma tupla (sucesso, mensagem).
    """
    nome = nome.strip()

    if quantidade_baixa <= 0:
        return False, "A quantidade a dar baixa precisa ser maior que zero."

    sucesso, motivo = usuario_model.dar_baixa_produto(nome, quantidade_baixa)

    if sucesso:
        quantidade_restante = usuario_model.consultar_quantidade(nome)
        if quantidade_restante is None:
            return True, f"Baixa registrada. Estoque de '{nome}' zerado e produto removido do catálogo."
        return True, f"Baixa registrada! Restam {quantidade_restante} unidades de '{nome}'."

    if motivo == "nao_encontrado":
        return False, f"Produto '{nome}' não foi encontrado."
    if motivo == "quantidade_insuficiente":
        return False, f"Estoque insuficiente para dar baixa em '{nome}'."
    return False, "Não foi possível dar baixa no produto."


def controlador_pesquisar_produto(nome):
    nome = nome.strip()

    if usuario_model.pesquisar_produto(nome):
        quantidade = usuario_model.consultar_quantidade(nome)
        return True, f"Produto encontrado: {nome} - quantidade: {quantidade}"
    return False, f"Produto '{nome}' não foi encontrado."


def controlador_listar_produtos():
    return usuario_model.listar_produtos()
#######################################################

def controlador_registrar_compra(nome, quantidade):
    """
    Regra de negócio para registrar uma compra.

    Regras aplicadas:
        1) Quantidade precisa ser maior que zero.
        2) Produto precisa existir.
        3) Quantidade comprada não pode ser maior que o estoque atual.

    Retorna uma tupla (sucesso, mensagem).
    """
    nome = nome.strip()

    if quantidade <= 0:
        return False, "A quantidade da compra precisa ser maior que zero."

    sucesso, motivo = usuario_model.registrar_compra(nome, quantidade)

    if sucesso:
        quantidade_restante = usuario_model.consultar_quantidade(nome)
        if quantidade_restante is None:
            return True, f"Compra registrada! Estoque de '{nome}' zerado e produto removido do catálogo."
        return True, f"Compra registrada! Restam {quantidade_restante} unidades de '{nome}'."

    if motivo == "nao_encontrado":
        return False, f"Produto '{nome}' não foi encontrado."
    if motivo == "quantidade_insuficiente":
        return False, f"Estoque insuficiente para registrar essa compra de '{nome}'."
    return False, "Não foi possível registrar a compra."


def controlador_atualizar_estoque(nome, quantidade_adicional):
    """
    Regra de negócio para atualizar (repor) o estoque de um produto.

    Regras aplicadas:
        1) Quantidade a adicionar precisa ser maior que zero.
        2) Produto precisa existir.

    Retorna uma tupla (sucesso, mensagem).
    """
    nome = nome.strip()

    if quantidade_adicional <= 0:
        return False, "A quantidade a adicionar precisa ser maior que zero."

    sucesso = usuario_model.atualizar_estoque(nome, quantidade_adicional)

    if sucesso:
        nova_quantidade = usuario_model.consultar_quantidade(nome)
        return True, f"Estoque atualizado! '{nome}' agora tem {nova_quantidade} unidades."
    return False, f"Produto '{nome}' não foi encontrado."
# ============================================================
# ARQUIVO: model/usuario_model.py
# ============================================================
# Camada MODEL (Modelo)
# ============================================================
from model.banco_dados import produtos, usuarios, salvar_produtos, compras,salvar_compras
from datetime import datetime
from model.banco_dados import produtos
from model.banco_dados import usuarios
from model.banco_dados import salvar_produtos


def gerar_novo_id():
    """
    Gera automaticamente o próximo ID de produto disponível,
    no formato "001", "002", "003"...
    """
    if not produtos:
        return "001"

    numeros = [int(info["id"]) for info in produtos.values()]
    proximo_numero = max(numeros) + 1

    return str(proximo_numero).zfill(3)


def inserir_produto(nome, quantidade):
    """
    Insere um novo produto no dicionário, gerando automaticamente
    o ID, e salva a alteração no arquivo JSON.

    Retorna o id_produto gerado, para a View poder exibi-lo.
    """
    id_produto = gerar_novo_id()
    produtos[nome] = {"id": id_produto, "quantidade": quantidade}
    salvar_produtos(produtos)
    return id_produto


def dar_baixa_produto(nome, quantidade_baixa):
   
   if nome not in produtos:
       return False, "nao_encontrado"
   
   quantidade_atual = produtos[nome]["quantidade"]

   if quantidade_baixa > quantidade_atual:
       return False, "quantidade_insuficiente"
   
   nova_quantidade = quantidade_atual - quantidade_baixa

   if nova_quantidade == 0:
       del produtos[nome]
    
   else:
       produtos[nome]["quantidade"] = nova_quantidade
    
   salvar_produtos(produtos)

   return True, "ok"

def registrar_compra(nome, quantidade):
    
    if nome not in produtos:
        return False, "nao_encontrado"

    quantidade_atual = produtos[nome]["quantidade"]

    if quantidade > quantidade_atual:
        return False, "quantidade_insuficiente"
    id_produto = produtos[nome]["id"]

    nova_quantidade = quantidade_atual - quantidade

    if nova_quantidade == 0:
        del produtos[nome]
    else:
        produtos[nome]["quantidade"] = nova_quantidade

    salvar_produtos(produtos)

    registro = {
        "produto": nome,
        "id_produto": id_produto,
        "quantidade": quantidade,
        "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    }
    compras.append(registro)
    salvar_compras(compras)

    return True, "ok"

def atualizar_estoque(nome, quantidade_adicional):
    """
    Soma uma quantidade ao estoque atual de um produto (reposição).

    Retorna:
        True  -> se o produto existia e foi atualizado.
        False -> se o produto não foi encontrado.
    """ 
    if nome not in produtos:
        return False
    produtos[nome]["quantidade"] += quantidade_adicional
    salvar_produtos(produtos)
    return True 


def pesquisar_produto(nome):
    """
    Verifica se um determinado produto (buscando pelo nome) já
    existe no dicionário.
    """
    if nome in produtos:
        return True
    return False


def consultar_quantidade(nome):
    """
    Retorna a quantidade em estoque de um produto, ou None se
    o produto não existir.
    """
    if nome in produtos:
        return produtos[nome]["quantidade"]
    return None


def listar_produtos():
    """
    Monta e retorna uma lista com todos os produtos cadastrados,
    no formato "id_produto - nome - quantidade: X" em cada linha.
    """
    lista_de_produtos = []

    for nome, info in produtos.items():
        lista_de_produtos.append(
            f"{info['id']} - {nome} - quantidade: {info['quantidade']}"
        )

    return lista_de_produtos


def validar_produto(nome, id_produto):
    """
    Confere se o produto existe e se o ID informado confere
    com o ID cadastrado.
    """
    if nome in produtos and produtos[nome]["id"] == id_produto:
        return True
    return False


def validar_login(login, senha):
    """
    Confere se o login existe e se a senha informada confere
    com a senha cadastrada.
    """
    if login in usuarios and usuarios[login] == senha:
        return True
    return False
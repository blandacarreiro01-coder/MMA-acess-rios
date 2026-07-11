# ============================================================
# ARQUIVO: model/usuario_model.py
# ============================================================
# Camada MODEL (Modelo)
#
# É a única camada do sistema que pode acessar diretamente o
# dicionário "usuarios", definido em model/banco_dados.py.
#
# As camadas View (telas) e Controller NUNCA devem mexer no
# dicionário diretamente. Elas sempre devem chamar uma função
# deste arquivo para isso.
#
# Cada função abaixo tem uma única responsabilidade, como pedido
# no enunciado do trabalho.
# ============================================================

from model.banco_dados import usuarios


def inserir_usuario(login, senha):
    """
    Insere um novo usuário no dicionário.

    Esta função apenas GRAVA os dados. Ela não verifica se o
    login já existe nem se os campos estão vazios — essa
    verificação é uma regra de negócio e fica por conta do
    Controller.
    """
    usuarios[login] = senha


def remover_usuario(login):
    """
    Remove um usuário do dicionário, caso ele exista.

    Retorna:
        True  -> se o usuário foi encontrado e removido.
        False -> se o usuário não existia no dicionário.
    """
    if login in usuarios:
        del usuarios[login]
        return True
    return False


def pesquisar_usuario(login):
    """
    Verifica se um determinado login já existe no dicionário.

    Retorna:
        True  -> se o login existe.
        False -> se o login não existe.
    """
    if login in usuarios:
        return True
    return False


def listar_usuarios():
    """
    Monta e retorna uma lista com todos os logins cadastrados.

    Importante: por segurança, esta função NUNCA retorna as
    senhas dos usuários, apenas os logins.
    """
    lista_de_logins = []

    # Percorre todas as chaves (logins) do dicionário
    for login in usuarios:
        lista_de_logins.append(login)

    return lista_de_logins


def validar_login(login, senha):
    """
    Confere se o login existe e se a senha informada confere
    com a senha cadastrada. Usada na tela de autenticação.

    Retorna:
        True  -> login e senha corretos.
        False -> login não existe OU senha incorreta.
    """
    if login in usuarios and usuarios[login] == senha:
        return True
    return False

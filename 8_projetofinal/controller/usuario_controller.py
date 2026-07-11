# ============================================================
# ARQUIVO: controller/usuario_controller.py
# ============================================================
# Camada CONTROLLER (Controlador)
#
# Esta camada fica "no meio de campo" entre a View (telas) e o
# Model (dados). É aqui que ficam as REGRAS DE NEGÓCIO do
# sistema, como por exemplo:
#
#   - não permitir login duplicado;
#   - não permitir campos vazios;
#   - não permitir remover o usuário administrador.
#
# As telas (View) nunca chamam o Model diretamente. Elas sempre
# chamam uma função deste Controller, e é o Controller quem
# decide se deve ou não chamar o Model.
# ============================================================

from model import usuario_model


def controlador_login(login, senha):
    """
    Regra de negócio da tela de login.

    Retorna True se o login e a senha estiverem corretos.
    """
    return usuario_model.validar_login(login, senha)


def controlador_inserir_usuario(login, senha):
    """
    Regra de negócio para inserir um novo usuário.

    Regras aplicadas:
        1) Login e senha não podem estar em branco.
        2) Não pode existir dois usuários com o mesmo login.

    Retorna uma tupla (sucesso, mensagem):
        sucesso  -> True ou False
        mensagem -> texto para ser exibido na tela
    """
    login = login.strip()
    senha = senha.strip()

    # Regra 1: campos obrigatórios
    if login == "" or senha == "":
        return False, "Login e senha não podem ficar em branco."

    # Regra 2: não permitir login duplicado
    if usuario_model.pesquisar_usuario(login):
        return False, f"O login '{login}' já está cadastrado."

    # Se passou pelas regras, o Controller manda o Model gravar
    usuario_model.inserir_usuario(login, senha)
    return True, f"Usuário '{login}' cadastrado com sucesso!"


def controlador_pesquisar_usuario(login):
    """
    Regra de negócio para pesquisar um usuário pelo login.

    Retorna uma tupla (encontrado, mensagem).
    """
    login = login.strip()

    if usuario_model.pesquisar_usuario(login):
        return True, f"Usuário encontrado: {login}"
    return False, f"Usuário '{login}' não foi encontrado."


def controlador_remover_usuario(login):
    """
    Regra de negócio para remover um usuário.

    Regra aplicada:
        - Não é permitido remover o usuário administrador (admin),
          para que o sistema nunca fique sem um usuário de acesso.

    Retorna uma tupla (sucesso, mensagem).
    """
    login = login.strip()

    if login == "admin":
        return False, "Não é permitido remover o usuário administrador."

    if usuario_model.remover_usuario(login):
        return True, f"Usuário '{login}' removido com sucesso!"
    return False, f"Usuário '{login}' não foi encontrado."


def controlador_listar_usuarios():
    """
    Regra de negócio para listar os usuários cadastrados.

    Apenas repassa a lista de logins vinda do Model para a View.
    """
    return usuario_model.listar_usuarios()

# ============================================================
# ARQUIVO: model/banco_dados.py
# ============================================================
# Este arquivo representa o "banco de dados" do nosso sistema.
#
# Como as regras do projeto não permitem o uso de banco de dados
# real, arquivos, JSON ou CSV, vamos guardar os usuários usando
# apenas um DICIONÁRIO Python, que fica em memória enquanto o
# programa está rodando.
#
# Estrutura do dicionário:
#
#   usuarios = {
#       "login1": "senha1",
#       "login2": "senha2"
#   }
#
# A CHAVE do dicionário é o login do usuário.
# O VALOR do dicionário é a senha do usuário.
# ============================================================

# Dicionário que guarda todos os usuários cadastrados no sistema.
# Ele já começa com o usuário administrador criado automaticamente,
# conforme pedido no enunciado do trabalho.
usuarios = {
    "admin": "123"
}

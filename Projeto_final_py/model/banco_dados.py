# ============================================================
# ARQUIVO: model/banco_dados.py
# ============================================================
# Este arquivo representa o "banco de dados" do nosso sistema.
#
# Os usuários continuam guardados em memória, num dicionário
# Python simples (login: senha).
#
# Já os produtos são persistidos em um arquivo JSON no disco,
# usando as funções carregar_produtos() e salvar_produtos().
#
# Estrutura do dicionário de produtos:
#
#   produtos = {
#       "Produto 1": {"id": "001", "quantidade": 10},
#       "Produto 2": {"id": "002", "quantidade": 5}
#   }
# ============================================================

import json
import shutil
import os

CAMINHO_ARQUIVO = "dados.json"
CAMINHO_BACKUP = "dados_backup.json"

usuarios = {
    "Marcelo": "marcelo123",
    "Márcio": "marcio123",
    "Admin": "admin123",
}

usuarios = {k.lower(): v for k, v in usuarios.items()}  # Converte todos os logins para minúsculas para evitar problemas de case-sensitive

def carregar_produtos():
    """
    Lê o arquivo JSON do disco e retorna os produtos como
    dicionário Python. Se o arquivo não existir ainda (primeira
    execução do programa), retorna um dicionário vazio.
    """
    try:
        with open(CAMINHO_ARQUIVO, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return {}


def salvar_produtos(produtos):
    """
    Grava o dicionário de produtos no arquivo JSON, sobrescrevendo
    o conteúdo anterior.

    Antes de sobrescrever, faz uma cópia de segurança do arquivo
    atual em dados_backup.json — assim, se o novo arquivo salvar
    corrompido ou algo der errado, dá pra recuperar a última
    versão válida.
    """
    # Faz backup do arquivo atual, se ele já existir
    if os.path.exists(CAMINHO_ARQUIVO):
        shutil.copyfile(CAMINHO_ARQUIVO, CAMINHO_BACKUP)

    with open(CAMINHO_ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(produtos, arquivo, indent=4, ensure_ascii=False)


produtos = carregar_produtos()
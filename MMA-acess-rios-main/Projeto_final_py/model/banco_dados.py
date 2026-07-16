# ============================================================
# ARQUIVO: model/banco_dados.py
# ============================================================
# Este arquivo representa o "banco de dados" do nosso sistema.
#
# Usuários: dicionário simples em memória (login: senha).
#
# Produtos: persistidos em dados.json.
# Compras: histórico persistido em dados_compras.json.
#
# Estrutura do dicionário de produtos:
#   produtos = {
#       "Produto 1": {"id": "001", "quantidade": 10}
#   }
#
# Estrutura da lista de compras:
#   compras = [
#       {"produto": "Produto 1", "id_produto": "001",
#        "quantidade": 3, "data": "13/07/2026 19:40:00"}
#   ]
# ============================================================

import json
import shutil
import os

CAMINHO_ARQUIVO = "dados.json"
CAMINHO_BACKUP = "dados_backup.json"

CAMINHO_COMPRAS = "dados_compras.json" 
CAMINHO_COMPRAS_BACKUP = "dados_compras_backup.json"

usuarios = {
    "Marcelo": "marcelo123",
    "Márcio": "marcio123",
    "Admin": "admin123",
    "Blanda": "Blanda123",
}

# usuarios = {k.lower(): v for k, v in usuarios.items()}  # Converte todos os logins para minúsculas para evitar problemas de case-sensitive

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
    Grava o dicionário de produtos no arquivo JSON, fazendo
    backup do conteúdo anterior antes de sobrescrever.
    """
    if os.path.exists(CAMINHO_ARQUIVO):
        shutil.copyfile(CAMINHO_ARQUIVO, CAMINHO_BACKUP)

    with open(CAMINHO_ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(produtos, arquivo, indent=4, ensure_ascii=False)

def carregar_compras():
    """
Lê o arquivo JSON do histórico de compras. Se ainda não existir,
retorna uma lista vazia
"""
    try:
        with open(CAMINHO_COMPRAS, "r", encoding="utf-8")as arquivo:
            return json.load(arquivo) 
    except FileNotFoundError:
        return[] 

def salvar_compras(compras):
    """ 
    Grava lista de compras no arquivo JSON,fazendo backup 
    do conteúdo anterior antes de sobrescrever
    """ 
    if os.path.exists(CAMINHO_COMPRAS):
        shutil.copyfile(CAMINHO_COMPRAS,CAMINHO_COMPRAS_BACKUP) 
    with open(CAMINHO_COMPRAS, "w", encoding="utf-8") as arquivo:
        json.dump(compras, arquivo, indent=4, ensure_ascii=False)  

produtos = carregar_produtos()
compras = carregar_compras()
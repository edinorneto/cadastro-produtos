import json
import os

def carregar_dados(caminho_arquivo):
    if os.path.exists(caminho_arquivo):
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            try:
                return json.load(arquivo)
            except json.JSONDecodeError:
                print("Arquivo corrompido ou mal formatado. Retornando lista vazia.")
                return []
    return []

def salvar_dados(caminho_arquivo, dados):
    with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)
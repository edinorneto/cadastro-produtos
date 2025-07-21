from config import ARQUIVO_JSON
from data import carregar_dados, salvar_dados
from interface import obter_dados_do_produto, exibir_mensagem

def main():
    produtos = carregar_dados(ARQUIVO_JSON)

    # Garante que irá pegar sempre o maior ID existente, mesmo se o JSON estiver fora de ordem
    ultimo_id = max((p.get("id", 0) for p in produtos), default=0)
    proximo_id = ultimo_id + 1

    novo_produto = obter_dados_do_produto(proximo_id)
    produtos.append(novo_produto)
    salvar_dados(ARQUIVO_JSON, produtos)
    exibir_mensagem("\nProduto cadastrado com sucesso!")

if __name__ == "__main__":
    main()
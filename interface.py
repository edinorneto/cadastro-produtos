from datetime import datetime
from zoneinfo import ZoneInfo

def ler_numero(msg, tipo=float):
    while True:
        try:
            entrada = input(msg)
            if tipo == float:
                entrada = entrada.replace(".", "").replace(",", ".")
            return tipo(entrada)
        except ValueError:
            print("Valor inválido. Tente novamente.")

def obter_dados_do_produto(proximo_id):
    br_time = datetime.now(ZoneInfo("America/Sao_Paulo"))
    ativo_input = input("Produto ativo? (s/n): ").strip().lower()
    ativo = ativo_input in ["s", "sim", "y", "yes"]
    produto = {
        "id": proximo_id,
        "nome": input("Nome do produto: "),
        "descricao": input("Descrição do produto: "),
        "preco": ler_numero("Preço do produto: R$ ", tipo=float),
        "categoria": input("Categoria do produto: "),
        "estoque": ler_numero("Quantidade em estoque: ", tipo=int),
        "unidade": input("Unidade (ex: un, kg, t): "),
        "ncm": ler_numero("NCM do produto: ", tipo=int),
        "ativo": ativo,
        "data_cadastro": br_time.strftime('%d/%m/%Y %H:%M')
    }
    return produto

def exibir_mensagem(msg):
    print(msg)
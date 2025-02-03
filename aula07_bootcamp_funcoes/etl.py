import csv

path_arquivo = "etl.csv"

def read_csv(nome_arquivo) -> list[dict]:
    """
    Função para ler arquivos csv
    """

    lista = []
    with open (nome_arquivo, mode="r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            lista.append(linha)
    return lista

def produtos_nao_entregues(lista: list[dict]) -> list[dict]:

    lista_filtrada = []
    for produto in lista:
        if produto.get("entregue") == "True":
            lista_filtrada.append(produto)
    return lista_filtrada

def somar_valores_produtos(lista_filtrada: list[dict]) -> int:

    valor_total = 0
    for produto in lista_filtrada:
        valor_total += int(produto.get("preco"))
    return valor_total
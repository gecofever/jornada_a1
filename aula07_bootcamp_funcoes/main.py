from etl import read_csv, produtos_nao_entregues, somar_valores_produtos

path_arquivo = "etl.csv"

itens_vendas: list[dict]

itens_vendas = read_csv(path_arquivo)
print(itens_vendas)

lista_de_produtos = read_csv(path_arquivo)
produtos_entregues = produtos_nao_entregues(lista_de_produtos)
print(produtos_entregues)

valor_produtos_entregues = somar_valores_produtos(produtos_entregues)
print(valor_produtos_entregues)
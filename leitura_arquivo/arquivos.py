import csv

path = r"C:\\Users\\Nascimento\\Germano\\Jornada de Dados\\bootcamp_python\\leitura_arquivo\\dados.csv"

dados = []

with open(path, mode="r", encoding='utf-8') as arquivo:
    leitor_csv = csv.DictReader(arquivo)

    for linha in leitor_csv:
        dados.append(linha)

for registro in dados:
    print(registro)
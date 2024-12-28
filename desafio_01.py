# 1
quant = int(input('Informe uma quantidade: '))
preco = float(input('Informa uma preco: '))

if (quant < 0) or (preco < 0):
    print('valores invalidos')
else:
    print('valores validos')

# 2
print()
log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}

if log['level'] == 'ERROR':
    print(log['message'])
else:
    print('Log OK!')

# 3
print()
idade = 29
email = 'germa@yahoo.com.br'

if idade < 25:
    print('Idade invalida')
elif (25 <= idade <= 65) and ('@' in email):
    print('Dados Validos...')
else:
    print('Dados Invalidos, verifique seus dados...')

# 4 (transação suspeita)
print()
transacao = {'valor': 12000, 'hora': 20}

if (transacao['valor'] > 10000) and (transacao['hora'] > 18):
    print('Transação suspeita...Alerta!')
else:
    print('Transação aceita!')

# 5 (contagem de palavras)
texto = 'Vamos fazer o teste com esse texto'

texto = texto.split()
palavras_contadas = {}

for t in texto:
    if t in palavras_contadas:
        palavras_contadas[t] += 1
    else:
        palavras_contadas[t] = 1
print(palavras_contadas)

# 6
print()
usuarios = [
    {"nome": "Alice", "email": "alice@example.com"},
    {"nome": "Bob", "email": ""},
    {"nome": "Carol", "email": "carol@example.com"}
]

usuarios_validos = [usuario for usuario in usuarios if usuario["email"]]

print(usuarios_validos)
print()

# 7
pagina_atual = 1
paginas_totais = 6

while pagina_atual <= paginas_totais:
    print(f"Processando página {pagina_atual} de {paginas_totais}")
    pagina_atual += 1

print("Todas as páginas foram processadas.")

# 8
print()
itens = [1, 2, 3, "parar", 4, 5]

for item in itens:
    if item == "parar":
        print(f'Item encontrado...{item}')
        break
    print(f'Processando item{item}')

# 9
print()
for i in range(1, 11):
    print(i ** 2)

# 10
print()
lista = ["Python", "Java", "C++", "JavaScript"]

lista.remove("C++")
print(lista)
lista.append("Ruby")
print(lista)
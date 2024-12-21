# 11
nome = input('Digite a palavra que iremos converter para maiusculo: ')
print(nome.capitalize())
print()

# 12
nome_completo = input('Digite seu nome completo: ')
print(nome_completo.upper())
print()

# 13
frase_curta = input('Digite uma frase curta com espaço no inicio e final: ')
print(frase_curta.strip())

# 14
data = input('Digite uma data no formato dd/mm/aa: ')
lista_data = data.split("/")
print(f'Dia: {lista_data[0]}')
print(f'Mês: {lista_data[1]}')
print(f'Ano: {lista_data[2]}')

# 15
palavra_1 = input('Primeira string: ')
palavra_2 = input('Segunda string: ')
frase = palavra_1 + ' ' + palavra_2
print(frase)
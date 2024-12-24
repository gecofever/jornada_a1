# 21
try:
    celsius = float(input('Digite uma temperatura em Celsius: '))
    farenheigt = (celsius * 1.8) + 32
    print(f'{farenheigt:.2f}')
except ValueError:
    print('Valor digitado incorreto')

# 22
print()
palavra = input('Forneça uma palavra: ')
if palavra.isdigit():
    print("Digite uma palavra, por favor")
else:
    palavra_tratada = palavra.replace(" ", "").lower()
    palavra_invertida = palavra_tratada[::-1]
    if palavra_tratada == palavra_invertida:
        print(f'{palavra}, é palidromo')
    else:
        print(f'{palavra}, não é palidromo')

# 23
print()
try:
    operacao = input('Escolha a operação matematica: ')
    number_1 = int(input('Digite um numero: '))
    number_2 = int(input('Digite o segundo numero: '))
    if operacao == '+':
        print(number_1 + number_2)
    elif operacao == '-':
        print(number_1 - number_2)
    elif operacao == '*':
        print(number_1 * number_2)
    elif operacao == '/' and number_2 != 0:
        print(number_1 / number_2)
    else:
        print('Digite opções validas! e divisor diferente de zero')
except:
    print("Digite um numero valido...")


# 24
print()
try:
    entrada = int(input('Digite um numero: '))
    if entrada > 0 and (entrada % 2 == 0):
        print('POSITIVO e Par')
    elif entrada < 0 and (entrada % 2 == 0):
        print('NEGATIVO e Par')
    elif entrada > 0 and (entrada % 2 != 0):
        print('POSITIVO e Impar')
    elif entrada < 0 and (entrada % 2 != 0):
        print('NEGATIVO e Impar')
    else:
        print('ZERO')
except ValueError:
    print('Favor digite um numero')


# 25
print()
lista = []

elemento = input('Digite 1 lista com 5 elementos: ')
elemento_str = elemento.split(",")

try:
    for int_elemento in elemento_str:
        lista.append(int(int_elemento.strip()))
    print(f'Lista de Inteiros: {lista}')
except ValueError:
    print('Favor digite um numeo inteiro...')
import time

# Exercicio 1

def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1

valores = [1, 2, 3, 4, 5]
dobra(valores)
print(valores)


# Exercicio 2 (Desempacotamento)

def soma(* valores):
    s = 0
    for numero in valores:
        s = s + numero
    print(f'Somando os valores {valores}, temos o resultado {s}')

soma(1, 2, 3)
soma(2, 2, 2, 2)

# Exercicio 3 (Area do terreno)

print()
largura = int(input('Digite largura do terreno: '))
comprimento = int(input('Digite comprimento do terreno: '))

def area(largura, comprimento):
    area = largura * comprimento
    print(f'A area do terreno mede: {area}m²')

area(largura, comprimento)

# Exercicio 4 (Comprimento e Escreva)

print()
mensagem = input('Escreva uma Mensagem: ')
size = len(mensagem) + 4

def escrever(msg):
    print('-' * size)
    print(f'  {msg}')
    print('-' * size)

escrever(mensagem)
print()

# Exercicio 5 - Contador

def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1 if inicio < fim else -1

    if (inicio < fim and passo < 0) or (inicio > fim and passo > 0):
        passo = -passo  # Ajusta o sinal do passo corretamente
    
    for contagem in range(inicio, fim + (1 if passo > 0 else -1), passo):
        print(f'{contagem} ', end='', flush=True)
        time.sleep(0.5)
    print('Fim!')

contador(1, 5, 1)
contador(8, 2, -2)
inicio = int(input('Inicio: '))
fim = int(input('Final: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)


# Função Maior

print()
lista_1 = [7, 5, 4, 1, 3]
lista_2 = [9, 5, 3]
lista_3 = [8, 3]
lista_4 = []

def maior(lista):
    if not lista:
        print("Sua lista contem 0 numeros. O maior deles é 0.")
        return

    for numero in lista:
        print(f'{numero} ', end='', flush=True)
        time.sleep(1)
    print(f'Sua lista contem {len(lista)} numeros. O Maior deles é {max(lista)}')

maior(lista_1)
maior(lista_2)
maior(lista_3)
maior(lista_4)
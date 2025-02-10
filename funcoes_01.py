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

# Exercicio 5 - Contador

def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1 if inicio < fim else -1

    if (inicio < fim and passo < 0) or (inicio > fim and passo > 0):
        passo = -passo  # Ajusta o sinal do passo corretamente
    
    for contagem in range(inicio, fim + (1 if passo > 0 else -1), passo):
        print(contagem)
        time.sleep(1)

contador(1, 10, 1)
contador(10, 1, -2)
inicio = int(input('Inicio: '))
fim = int(input('Final: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
print('Estudando com o Luciano')

nome = input('Digite seu nome: ')
print(len(nome))

valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
soma = valor1 + valor2
print(soma)

nome_usuario = input('Digite seu nome: ')
salario = float(input('Informe seu salario: R$'))
bonus = float(input('Informe o percentual do bônus recebido: '))

kpi = 1000 + (salario * bonus)

print(f'{nome_usuario}, o valor total a receber é {kpi}')
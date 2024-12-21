# 16 e 17
expressao_1 = input('True ou False: ').strip().lower()
expressao_2 = input('True ou False: ').strip().lower()

if expressao_1 == "true":
    expressao_1 = True
else:
    expressao_1 = False

if expressao_2 == "true":
    expressao_2 = True
else:
    expressao_2 = False

result = expressao_1 and expressao_2
result_2 = expressao_1 or expressao_2

print(f"O resultado de ({expressao_1}) AND ({expressao_2}) é: {result}")
print(f"O resultado de ({expressao_1}) OR ({expressao_2}) é: {result_2}")

# 18
expressao_3 = False
result_3 = not expressao_3
print(f'Invertendo temos: {result_3}')
print()

# 19 e 20

number_1 = int(input('Digite um numero de 1 a 15: '))
number_2 = int(input('Digite um numero de 1 a 15: '))

compare = (number_1 == number_2)
compare_2 = (number_1 != number_2)
print(f'Resultado da igualdade: {compare}')
print(f'Resultado da diferença: {compare_2}')
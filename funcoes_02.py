# Votação

def votacao(ano):

    idade = 2025 - ano
    if idade < 18:
        print(f'Com {idade} anos: Você não vota')

    elif idade > 18 and idade < 70:
        print(f'Com {idade} anos: Voto Obrigatório')
    else:
        print(f'Com {idade} anos: Voto Opcional')

votacao(ano = int(input('Em que ano você nasceu: ')))
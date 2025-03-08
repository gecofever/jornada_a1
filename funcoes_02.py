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


# Fatorial

print()
def fatorial(num=1, show=True):
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if show:
            print(c, end='')
            if ( c > 1 ):
                print(' x ', end='')
            else:
                print(' = ', end='')
    return f

n = int(input('Digite um numero: '))
print(fatorial(n, True))


# Ficha Jogador

print()
def ficha(nome='<desconhecido>', gols=0):
    print(f'O Jogador {nome} marcou {gols} gols')

player_name = input("Informe nome do Jogador: ")
scored_gols = str(input("Gols marcados: "))

if scored_gols.isnumeric():
    scored_gols = int(scored_gols)
else:
    scored_gols = 0
if player_name.strip() == '':
    ficha(gols=scored_gols)
else:
    ficha(player_name, scored_gols)
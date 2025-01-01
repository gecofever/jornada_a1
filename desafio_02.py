# 1
livros = {
    1: {"Titulo": "Apaixone-se pelo problema", "Autor": "Uri Levine", "Ano": 2024},
    2: {"Titulo": "Storytelling", "Autor": "Mikael", "Ano": 2018},
    3: {"Titulo": "Scrum Master", "Autor": "Jeff Schawber", "Ano": 2021},
}

print(livros[1])
print(livros[2]["Titulo"])

# 2
texto = "A Morenhinha by Jose de Alencar"

palavras_contadas = {}

for caractere in texto:
    palavras_contadas[caractere] = palavras_contadas.get(caractere, 0) + 1
print(palavras_contadas)

# 3
lista_compras = ["maçã", "banana", "cereja"]
precos = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}
quantidades = [3, 10, 6]

total = sum(precos[item] * quantidade for item, quantidade in zip(lista_compras, quantidades))
print(f"Preço total: {total:.2f}")

# 4
emails = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]
email_duplicados = set(emails)
print(email_duplicados)

# 5
idades = [22, 15, 30, 17, 18]
idades_validas = [idade for idade in idades if idade >= 18]

print(idades_validas)

# 6
print()
pessoas = [
    {"nome": "Bob", "idade": 30},
    {"nome": "Alice", "idade": 25},
    {"nome": "Carol", "idade": 20}
]
pessoas.sort(key=lambda pessoa: pessoa["nome"])
print(pessoas)

# Desafio aula_3

# Iniciar Variaveis
nome_valido = False
salario_valido = False
bonus_valido = False
funcionarios = {}

while not nome_valido:
    try:
        nome = input("Digite seu nome: ")

        # Verifica se o nome está vazio
        if len(nome) == 0:
            raise ValueError("O nome não pode estar vazio.")
        # Verifica se há números no nome
        elif any(char.isdigit() for char in nome):
            raise ValueError("O nome não deve conter números.")
        else:
            print("Nome válido:", nome)
            nome_valido = True
            funcionarios['nome'] = nome
    except ValueError as e:
        print(e)

# Solicita ao usuário que digite o valor do seu salário e converte para float

while not salario_valido:
    try:
        salario = float(input("Digite o valor do seu salário: "))
        if salario < 0:
            print("Por favor, digite um valor positivo para o salário.")
        else:
            salario_valido = True
            funcionarios['salario'] = salario
    except ValueError:
        print("Entrada inválida para o salário. Por favor, digite um número.")

# Solicita ao usuário que digite o valor do bônus recebido e converte para float
while not bonus_valido:
    try:
        bonus_recebido = float(input("Digite o valor do bônus recebido: "))
        if bonus_recebido < 0:
            print("Por favor, digite um valor positivo para o bônus.")
        else:
            bonus_valido = True
            funcionarios['bonus'] = bonus_recebido
    except ValueError:
        print("Entrada inválida para o bônus. Por favor, digite um número.")

# Assumindo uma lógica de cálculo para o bônus final e KPI
bonus_final = bonus_recebido * 1.2  # Exemplo, ajuste conforme necessário
kpi = (salario + bonus_final) / 1000  # Exemplo simples de KPI

# Imprime as informações para o usuário
print(f"Seu KPI é: {kpi:.2f}")
print(funcionarios)
print(f"{nome}, seu salário é R${salario:.2f} e seu bônus final é R${bonus_final:.2f}.")
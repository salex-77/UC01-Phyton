# Programa para encontrar o nome da pessoa mais jovem entre dez pessoas

# Lista para armazenar os nomes e idades
pessoas = []

# Solicitar ao usuário que insira o nome e a idade de dez pessoas
for i in range(10):
    nome = input(f"Digite o nome da pessoa {i+1}: ")
    idade = int(input(f"Digite a idade de {nome}: "))
    pessoas.append((nome, idade))

# Encontrar a pessoa mais jovem
pessoa_mais_jovem = min(pessoas, key=lambda x: x[1])

# Exibir o nome da pessoa mais jovem
print(f"A pessoa mais jovem é {pessoa_mais_jovem[0]} com {pessoa_mais_jovem[1]} anos.")

# Programa para encontrar pessoas que moram em "Campo Grande"

# Lista para armazenar os dados das pessoas
pessoas = []

# Solicitar ao usuário que insira o nome, telefone e cidade de dez pessoas
for i in range(10):
    nome = input(f"Digite o nome da pessoa {i+1}: ")
    telefone = input(f"Digite o telefone de {nome}: ")
    cidade = input(f"Digite a cidade de {nome}: ")
    pessoas.append((nome, telefone, cidade))

# Filtrar e exibir as pessoas que moram em "Campo Grande"
print("\nPessoas que moram em Campo Grande:")
for pessoa in pessoas:
    if pessoa[2].lower() == "campo grande":
        print(f"Nome: {pessoa[0]}, Telefone: {pessoa[1]}")

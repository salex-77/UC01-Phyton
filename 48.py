# Programa para encontrar pessoas que moram em "Campo Grande"

# Lista para armazenar os dados das pessoas
pessoas = []

# Solicitar ao usuário que insira o nome, telefone e cidade de dez pessoas
for i in range(10):
    nome = input(f"Digite o nome da pessoa {i+1}: ")  
    cidade = input(f"Digite a cidade de {nome}: ")
    pessoas.append((nome,cidade))

# Filtrar e exibir as pessoas que moram em "Campo Grande"
print("\nnome em ordem alfabetica:")
for pessoa in pessoas:
    if pessoa[2].lower() == "campo grande":
        print(f"Nome: {pessoa[0]}, Telefone: {pessoa[1]}")
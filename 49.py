def obter_dados_alunos():
    alunos = []
    for i in range(5):
        nome = input(f"Digite o nome do aluno {i+1}: ")
        while True:
            try:
                media = float(input(f"Digite a média do aluno {i+1} (entre 0 e 10): "))
                if 0 <= media <= 10:
                    break
                else:
                    print("A média deve estar entre 0 e 10. Tente novamente.")
            except ValueError:
                print("Valor inválido. Digite um número entre 0 e 10.")
        alunos.append((nome, media))
    return alunos

def main():
    alunos = obter_dados_alunos()
    print("\nLista de Alunos:")
    for nome, media in alunos:
        print(f"Nome: {nome}, Média: {media}")

if __name__ == "__main__":
    main()

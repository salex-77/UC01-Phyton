def media(n1,n2,n3,n4):
    media=(n1,n2,n3,n4)/4
    if(media>=7):
        return "aprovado"
    elif(media<7 and media>4):
        return "em recuperação"
    else:
        return "reprovado"    
    
def DefineMedia(nome):    
    notas=[]
    for i in range(4):
        notas.append(float(input(f"digite a {i+1}ª nota: ")))
    print(f'o aluno {nome} está: {media(notas[0],notas[1],notas[2]),notas[3]}')    

for i in range(5):
    nomeAluno=input("digite o nome do aluno:  ")
DefineMedia(nomeAluno)
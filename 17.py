nota1=float(input("digite sua nota "))
nota2=float(input("digite sua nota "))
media=(nota1+nota2)/2
print(f"média:{media}")
if(media<4):
    print("Aluno reprovado")
elif(media>=7):
    print("aluno aprovado direto")
else:
    print("aluno em recuperação")

recuperação=float(input(" nota "))
if(media<5):
    print("reprovado na recuperação")
else:
    print("aprovado na recuperação")    


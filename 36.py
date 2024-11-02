import random
def Game(numero):
    player2=random.randint(0,5)
    if (player2+numero) % 2 ==0:
        return 'PAR - Player1 venceu'
    else:
        return 'IMPÁR - pLAYER2 venceu'

print("jogo - par ou impar")
print("numero permitidos - 0,1,2,3,4, ou 5 ")
print()
print('-------------------------------')
print()
jogadas=int(input('quantas vezes deseja jogar: '))
for i in range(jogadas):
    player1=int(input("insira sua jogada: "))    
    print(f"{Game(player1)}")
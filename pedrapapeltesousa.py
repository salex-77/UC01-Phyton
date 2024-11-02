import random

lista = ['pedra', 'papel', 'tesoura']


player1=input("Escolha sua opção entre pedra papel e tesousa:  ")
player2=random.choice(lista)

if(player1==player2):
    print("empate")
elif(player1=="pedra" and player2=="tesoura") or (player1=="papel" and player2=="pedra") or (player1=="tesoura" and player2=="papel"):
    print(f"player1 venceu!! {player1} vence de {player2}")
else:
    print(f'player2 venceu!! {player2} vence de {player1}')
 

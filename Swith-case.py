# value=3
# match value:

#     case 1:
#         result="one"
#     case 2:
#         result='two'
#     case 3:
#         result="there"
#     case _:
#         result='defaul'
# print(result)
total=0

escolha=0
while(escolha!=5):
    print("cardapio: ")
    print("1-calabresa com cebola - R$40,00\n2-camarão com queijo - R$55,00\n3-frango com queijo - R$78,00\n4-banana com chocolate - R$99,00")
    print("5-finalizar pedido")

    escolha=int(input("digite a opção escolhida(apenas um numero):")) 

    match escolha:
    
        case 1:
            print("calabresa com cebola - R$40,00")
            total+=40.00
        case 2:
            print('camarão com queijo - R$55,00')
            total+=55.00
        case 3:
            print("frango com queijo - R$78,00")
            total+=78.00    
        case 4:
            print("banana com chocolate - R$99,00")    
            total+=99.00
        case 5:
            print(f"total do pedido: R${total}")    
        case _:
            print("escolha uma opção valida!! ")



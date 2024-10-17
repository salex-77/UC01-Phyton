# a=int(input("digite o primeiro número "))
# b=int(input("digite o primeiro número "))
# c=int(input("digite o primeiro número "))

# if(a>b):
#     if(a>c):
#         print("o primeiro é o maior")
#     else:
#         print("o terceiro é o maior")
# elif(b>c):
#     print("o segundo é o maior")        
# else:
#     print("terceiro é o maior")


# a=int(input("digite o primeiro número "))
# b=int(input("digite o primeiro número "))
# c=int(input("digite o primeiro número "))

# if(a==b and a==c):
#     print('os 3 valores são iguais')

# elif(a>b and a>c):
#     print("o primeiro é o maior")
# elif(b>c):
#     print("o segundo é o maior")
# else:
#     print("o terceiro é o maior ")

a=int(input("digite o primeiro número ")) 
b=int(input("digite o primeiro número "))
c=int(input("digite o primeiro número "))

valores=[a,b,c]
valores.sort()
valores.reverse()
print(valores[0])

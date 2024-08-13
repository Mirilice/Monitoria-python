# Para construir esse programa, considere que usuário só
# informará números inteiros positivos. Crie um programa que
# receba 5 números digitados e, ao fim, exibir quantos números
# são pares.

pares = 0
# quant = 0
# #opcao 1: com verificacao
# while True:
#     if quant == 5:
#         break
#     numero = int(input("Escreva um número inteiro positivo:"))
#     if numero > 0:  
#         quant+=1
#         if numero % 2 == 0: #Isso verifica se o número é par
#             pares += 1
#     else: print("Esse número não foi contabilizado pois é negativo")

# print(f"Foram digitados {pares} números pares.")
    
#opcao 2
for i in range(5):
    print("Escreva um número inteiro positivo:")
    numero = int(input())
    if numero < 1:
        print("Número negativo!")
        break
    if numero % 2 == 0: #Isso verifica se o número é par
        pares += 1

print(f"Foram digitados {pares} números pares.")
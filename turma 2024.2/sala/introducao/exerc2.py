# Faça um programa que peça dois números e imprima a soma.
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

#opcao1
soma = num1 + num2
print("A soma dos dois números é", soma) #ou usar o f"" aqui também está correto

#opcao2
print(f"A soma dos dois números é {num1 + num2}")

#opcao3
print("A soma dos dois números é", num1 + num2)

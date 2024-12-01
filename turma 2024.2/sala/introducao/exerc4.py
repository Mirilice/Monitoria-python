# Faça um programa que leia duas notas de um aluno de
# programação. Em seguida, calcule a média ponderada, com
# pesos 2 e 3, respectivamente. Por fim, o programa deve
# imprimir a média obtida.

nota1 = float(input("Nota 1: "))

nota2 = float(input("Nota 2: "))

mediaPonderada = (nota1*2 + nota2*3)/5

print(f"Média ponderada: {mediaPonderada}")


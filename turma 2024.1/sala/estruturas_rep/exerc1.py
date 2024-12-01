# Crie um programa no qual o usuário informe um valor N.
# Armazene esse valor em um variável chamada N.   

#variavel N: quantidade de números e quantidade de vezes que o
#for vai rodar
soma = 0
N = int(input('Informe N: '))
for i in range(N):
    # Em seguida, o usuário deve digitar N números.
    numero = float(input("Digite um número: "))
    soma += numero

# Ao fim, o programa deve
# imprimir a média aritmética dos N números digitados.
media = soma/N 

print(f"Se foram digitandos {N} números e a soma dos números digitados por você deu {soma}, então...")
print("Média dos números digitados:", media)



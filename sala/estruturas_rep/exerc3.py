# C# e a quantidade de
# mulheres de qualquer idade.onstrua um programa que receba o sexo e a idade de alunos
# de uma turma. Considere que o usuário não sabe quantos
# alunos existem na turma. Ao fim, o programa deve exibir a
# quantidade de homens acima de 18 anos e a quantidade de
# mulheres de qualquer idade. Para que o programa seja
# encerrado, o usuário deve informar uma idade negativa.

#while, tradução: enquanto

homem = 0
mulher = 0
#FOR -> COSTUMA SER USADO QUANDO SABEMOS QUANTAS VEZES VAI ACONTECER O EVENTO 

#WHILE -> COSTUMA SER USADO QUANDO NÃO SABEMOS QUANTAS VEZES VAI ACONTECER O EVENTO.
#PODE SER 1, 100, 10000, 0 VEZES. É O EXEMPLO DESSE EXERCÍCIO

idade = 1
while idade > 0:
    idade = int(input("Idade do aluno"))
    if idade < 0: 
        break
    sexo = input("Sexo do aluno(a)")

#Ao fim, o programa deve exibir a
# quantidade de homens acima de 18 anos     
    if sexo == "M" and idade > 18: #verificação se é homem e maior de 18
        homem+=1

#e a quantidade de
# mulheres de qualquer idade.
    elif sexo == "F": 
        mulher+=1

print(f"Há {homem} homem(ns) maiores de 18 anos e {mulher} mulher(es) de qualquer idade")
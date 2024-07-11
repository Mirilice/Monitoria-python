salario = float(input())

if (salario >= 0 and salario <= 400):
    bonus = 15
elif (salario >= 400.01 and salario <= 800):
    bonus = 12
elif (salario >= 800.01 and salario <= 1200):
    bonus = 10
elif (salario >= 1200.01 and salario <= 2000):
    bonus = 7
else: bonus = 4

reajuste = (bonus/100)*salario
novo_salario = salario + reajuste

print(f'Novo salario: {novo_salario:.2f}')
print(f'Reajuste ganho: {reajuste:.2f}')
print(f'Em percentual: {bonus} %')

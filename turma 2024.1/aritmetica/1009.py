nome = input()
salario_fixo = float(input())
total_vendas = float(input())

comissao = 0.15*total_vendas
total = salario_fixo + comissao

print(f'TOTAL = R$ {total:.2f}')
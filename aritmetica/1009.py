nome = input("Seu nome:")
salario_fixo = float(input('Qual é seu salário?'))
total_vendas = float(input('Quanto em reais você vendeu no mês?'))

comissao = 0.15*total_vendas
total = salario_fixo + comissao

print(f'NOME: {nome}')
print(f'R$ {total}')
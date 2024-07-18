# questão 1

#Faça um programa que converta metros para centímetros

#1m = 100cm


altura = float(input())

altura_em_centimetros = altura*100

print(f'{altura_em_centimetros}cm')

#Exemplo exponenciação

valor = 2
valor**(1/3)
valor**(1/2)

#Importancia sobre constantes

PI = 3.14

raio = float(input())

area_circulo = PI*(raio**2)

print(area_circulo)

#ganho por horas

# 1 real por hora
# 176 horas mensais 

hora = float(input())
trabalho = float(input())

salario = hora*trabalho

print(f'{salario} reais')

#len()

#opcoes

string1 = 'Brasil Hexa 2006'
string2 = 'Brasil! Hexa 2006!'

comp1 = len(string1)
print(comp1)
print(len(string1))
print(len('Brasil Hexa 2006'))
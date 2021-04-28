# 14 - João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
print("Exericio 14")
p14 = float(input("Digite o peso do peixe: "))
multa = 4.00
if p14 > 50 :
    e = p14-50
    print(f"o Valor da Multa é de: {e*multa:6.2f}")
else : 
    print("Peixe dentro do peso estipulado")


# 15 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#+ Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R$
#Obs.: Salário Bruto - Descontos = Salário Líquido.
print("Exericio 15")
h = float(input("Quanto você Ganha por Hora? "))
ht = float(input("Quantas horas você trabalha por mês? "))
# 15.A - salário bruto.
sb = (h*ht)
print("seu salario bruto é de: R$",sb)
# 15.B - quanto pagou ao INSS.
inss = sb*(8/100)
print("você pagou ao INSS, R$",inss)
# 15.C - quanto pagou ao sindicato.
sind = sb*(5/100)
print("você pagou ao Sindicato, R$", sind)
# IR
ir = sb*(11/100)
print("foi descontado o valor de R$",ir," Referente o Imposto de Renda")
# 15.E - -calcule os descontos e o salário líquido, conforme a tabela abaixo:
desc = (inss+sind+ir)
print("O Total de desconto foi de: R$",desc)
# 15.D - o salário líquido.
sl = sb-desc
print("O Valor do seu salario liquido é de: R$",sl)

# 16 - Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
print("Exericio 16")
m = float(input("Quantos metros quadrados tem o ambiente a ser pintado? "))
litro = (m/3)
preco = 80.00
latas = round(litro/18+0.5)
total = latas*preco
print("você ira precisar de ", latas," latas, o custo total é de: %.2f"%total)


# 17 - Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
#misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
import math
print("Exericio 17")
m17 = float(input("Quantos metros quadrados tem o ambiente a ser pintado? "))
l17 = (m/6)
litro17 = round((((10/100)*l17)+l17)+0.5)
lata18 = round(litro17/18+0.5)
preco18 = float(80.00)
lata3 = round(litro17/3.6+0.5)
preco3 = float(25.00)
print("você precisarar comprar ", litro17, "litros de tinta, temos três opçoes")
print("você pode comprar ", lata18, "latas de 18 litros, com um custo total de R$",(lata18*preco18))
print("você pode comprar ", lata3, "latas de 3.6 litros, com um cuto total de R$",(lata3*preco3))
m18 = round(litro17 / 18-0.5)
m3  = round((litro17 %18)/3.6+0.5)
ct = (m18*preco18)+(m3*preco3)
print("ou você pode comprar ", m18, "latas de 18 litros, e mais ", m3," latas de 3.6 litros, com um custo total de R$%.2f"%ct)

# 18 - Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos)
print("Exericio 18")
mb = float(input("Digite o tamanho do arquivo em MB "))
vel = float(input("Digite a velociadade da internet (Mbps) "))
tempo = (mb/(vel/8))/60
print("O Tempo para Download desse arquivo é de: %.2f"% tempo, "minutos")

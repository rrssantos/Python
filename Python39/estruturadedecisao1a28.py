# 1 - Faça um Programa que peça dois números e imprima o maior deles.

a1 = int(input("Digite um numero: "))
b1 = int(input("Digite um numero: "))

if a1 > b1 :
    print("O primeiro numero digitado é o maior ", a1)
else :
    print("O segundo numero digitado é o maior ", b1)

# 2 - Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
print("")
a2 = int(input("Digite um numero: "))

if (a2 >= 0) :
    print("O Numero digitado é positivo", a2)
else :
    print("O Numero digitado é negativo", a2)

# 3 - Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
print("")

a3 = input("Digite seu sexo (F/M): ")
a3 = a3.upper()
if (a3 == 'F') :
    print("Você é do sexo Feminino")
else :
    print("Você é do sexo Masculino")

# 4 - Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
print("")
a4 = input("Digite uma letra: ")
a4 = a4.lower()
if (a4 == 'a') or (a4 == 'e') or (a4 == 'i') or (a4 == 'o') or (a4 == 'u') :
    print("A letra digitada é uma Vogal :", a4)
else :
    print("A letra digitada é uma Consoante : ", a4)

if a4 in ('aeiou') :
    print("A letra digitada é uma Vogal : ", a4)
else :
    print("A letra digitada é uma Consoante : ", a4)

# 5 - Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
#A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#A mensagem "Reprovado", se a média for menor do que sete;
#A mensagem "Aprovado com Distinção", se a média for igual a dez.
print("")
a5 = float(input("Digite a nota do primeiro semestre: "))
b5 = float(input("Digite a nota do segundo semestre: "))
c5 = (a5+b5)/2
if c5 >= 7 and c5 < 10 :
    print("Aluno Aprovado, nota final: ", c5)
elif c5 < 7 :
    print("Aluno Reprovado, nota final: ", c5)
elif c5 == 10 :
    print("Alundo Aprovado com Distinção, notal final: ", c5 ,"Parabens")


# 6 - Faça um Programa que leia três números e mostre o maior deles.

a6 = int(input("Digite o primeiro numero: "))
b6 = int(input("Digite o segundo numero: "))
c6 = int(input("Digite o terceiro numero: ")) 
print("")
d6 = max(a6, b6, c6)
print("O Maior numero digitado foi: ", d6)

# 7 - Faça um Programa que leia três números e mostre o maior e o menor deles.
print("")

a7 = int(input("Digita o primeiro numero: "))
b7 = int(input("Digite o segundo numero: "))
c7 = int(input("Digite o terceiro numero: "))
print("")
d7 = min(a7, b7, c7)
print("O Menor numero digitado foi: ", d7)

# 8 - Faça um programa que pergunte o preço de três produtos e informe qual produto você deve
#comprar, sabendo que a decisão é sempre pelo mais barato.
print("")

a8 = float(input("Digite o valor do primeiro produto R$"))
b8 = float(input("Digite o valor do segundo produto R$"))
c8 = float(input("Digite o valor do terceiro produto R$"))
print("")
d8 = min(a8, b8, c8)
if (d8 == a8) : 
    print("O produto mais barato é o primeiro, R$",a8)
elif(d8 == b8) :
    print("O produto mais barato é o segundo, R$",b8)
else :
    print("O produto mais barato é o terceiro, R$",c8)

# 9 - Faça um Programa que leia três números e mostre-os em ordem decrescente.
print("")
lista = []

a9 = int(input("Digite o primeiro numero: "))
b9 = int(input("Digite o segundo numero: "))
c9 = int(input("Digite o terceiro numero: "))
lista.append(a9)
lista.append(b9)
lista.append(c9)

d9 = sorted(lista, reverse= True)
print(d9)

# 10 - Faça um Programa que pergunte em que turno você estuda. Peça para digitar
#M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!"
#ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

a10 = input("Digite o turno em que você estuda: ( M - Matutino, V- Verspetino, N - Noturno:) ")
a10 = a10.upper()
if (a10 == "M"):
    print("Bom Dia!")
elif(a10 == "V"):
    print("Boa Tarde!")
elif(a10 == "N") :
    print("Boa Noite!")
else :
    print("Opção Inválida")


# 11 - As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores
#e lhe contraram para desenvolver o programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte
#critério, baseado no salário atual:
#salários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento


a11 = float(input("Digite o valor do salario, R$: "))

if (a11 <= 280.00) :
    b11 = a11 * 0.20
    c11 = a11 + b11
    print("O Valor do Salario Atual é: R$ %.2f"% a11)
    print("O Valor do percentual aplicado é de: 20%")
    print("O Valor do aumento é de: R$ %.2f"% b11)
    print("O Valor do Novo Salario será: R$ %.2f"% c11)
elif(a11 < 700.00) :
    b11 = a11 * 0.15
    c11 = a11 + b11
    print("O Valor do Salario Atual é: R$ %.2f"% a11)
    print("O Valor do percentual aplicado é de: 15%")
    print("O Valor do aumento é de: R$ %.2f"% b11)
    print("O Valor do Novo Salario será: R$%.2f"%  c11)
elif(a11 < 1500.00) :
    b11 = a11 * 0.10
    c11 = a11 + b11
    print("O Valor do Salario Atual é: R$ %.2f"% a11)
    print("O Valor do percentual aplicado é de: 10%")
    print("O Valor do aumento é de: R$ %.2f"% b11)
    print("O Valor do Novo Salario será: R$ %.2f"% c11)
else :
    b11 = a11 * 0.05
    c11 = a11 + b11
    print("O Valor do Salario Atual é: R$ %.2f"% a11)
    print("O Valor do percentual aplicado é de: 5%")
    print("O Valor do aumento é de: R$ %.2f"% b11)
    print("O Valor do Novo Salario será: R$ %.2f"% c11)


#12 - Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são
#do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o
#Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado
#(é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos.
#O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
#Desconto do IR:
#Salário Bruto até 900 (inclusive) - isento
#Salário Bruto até 1500 (inclusive) - desconto de 5%
#Salário Bruto até 2500 (inclusive) - desconto de 10%
#Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações,
print("")
a12 = float(input("Digite o valor que recebe por hora trabalhada: "))
b12 = float(input("Digite a quantidade de horas trabalhada no mês: "))
c12 = a12 * b12

if c12 <= 900 :
    d12 = c12 * 0.03
    e12 = c12 * 0.11
    f12 = c12 * 0.10
    g12 = f12 + d12
    h12 = c12 - g12
    print("Salario Bruto, (", a12 ,"*",b12,")      R$: %.2f"% c12)
    print("IR (isento)                             R$:  0 ")
    print("(-) Sindicato                           R$: %.2f"% d12)
    print("(-) INSS                                R$: %.2f"% f12)
    print("FGTS                                    R$: %.2f"% e12)
    print("")
    print("Total de Descontos                      R$: %.2f"% g12)
    print("")
    print("Salario Liquido                         R$: %.2f"% h12)
elif c12 <= 1500 :
    i12 = c12 * 0.05
    d12 = c12 * 0.03
    e12 = c12 * 0.11
    f12 = c12 * 0.10
    g12 = f12 + d12 + i12
    h12 = c12 - g12 
    print("Salario Bruto, (",a12, "*",b12,")       R$: %.2f"% c12)
    print("(-) IR                                  R$: %.2f"% i12)
    print("(-) Sindicato                           R$: %.2f"% d12)
    print("(-) INSS                                R$: %.2f"% f12)
    print("FGTS                                    R$: %.2f"% e12)
    print("")
    print("Total de Descontos                      R$: %.2f"% g12)
    print("")
    print("Salario Liquido                         R$: %.2f"% h12)
elif c12 <= 2500 :
    i12 = c12 * 0.10
    d12 = c12 * 0.03
    e12 = c12 * 0.11
    f12 = c12 * 0.10
    g12 = f12 + d12 + i12
    h12 = c12 - g12 
    print("Salario Bruto, (",a12,"*",b12,")        R$: %.2f"% c12)
    print("(-) IR                                  R$: %.2f"% i12)
    print("(-) Sindicato                           R$: %.2f"% d12)
    print("(-) INSS                                R$: %.2f"% f12)
    print("FGTS                                    R$: %.2f"% e12)
    print("")
    print("Total de Descontos                      R$: %.2f"% g12)
    print("")
    print("Salario Liquido                         R$: %.2f"% h12)
else :
    i12 = c12 * 0.20
    d12 = c12 * 0.03
    e12 = c12 * 0.11
    f12 = c12 * 0.10
    g12 = f12 + d12 + i12
    h12 = c12 - g12 
    print("Salario Bruto, (",a12, "*",b12,")       R$: %.2f"% c12)
    print("(-) IR                                  R$: %.2f"% i12)
    print("(-) Sindicato                           R$: %.2f"% d12)
    print("(-) INSS                                R$: %.2f"% f12)
    print("FGTS                                    R$: %.2f"% e12)
    print("")
    print("Total de Descontos                      R$: %.2f"% g12)
    print("")
    print("Salario Liquido                         R$: %.2f"% h12)

# 13 - Faça um Programa que leia um número e exiba o dia correspondente
#da semana. (1-Domingo, 2- Segunda, etc.),
#se digitar outro valor deve aparecer valor inválido.

a13 = int(input("Digite um numero: "))

if a13 == 1 :
    print("O dia da semana correspondente ao numero é: Domingo")
elif a13 == 2 :
    print("O dia da semana correspondente ao numero é: Segunda-Feira")
elif a13 == 3 :
    print("O dia da semana correspondente ao numero é: Terça-Feira")
elif a13 == 4 :
    print("O dia da semana correspondente ao numero é: Quarta-Feira")
elif a13 == 5 :
    print("O dia da semana correspondente ao numero é: Quinta-Feira")
elif a13 == 6 :
    print("O dia da semana correspondente ao numero é: Sexta-Feira")
elif a13 == 7 :
    print("O dia da semana correspondente ao numero é: Sabado")
else :
    print("Numero inválido!")

# 14 - Faça um programa que lê as duas notas parciais obtidas por um aluno numa
#disciplina ao longo de um semestre, e calcule a sua média.
#A atribuição de conceitos obedece à tabela abaixo:
#  Média de Aproveitamento  Conceito
#  Entre 9.0 e 10.0        A
#  Entre 7.5 e 9.0         B
#  Entre 6.0 e 7.5         C
#  Entre 4.0 e 6.0         D
#  Entre 4.0 e zero        E
#O algoritmo deve mostrar na tela as notas, a média,
#o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C
#ou “REPROVADO” se o conceito for D ou E.
print("")
a14 = float(input("Digite a Primeira Nota: "))
b14 = float(input("Digite a Segunda Nota: "))
c14 = ((a14 + b14)/2)

if c14 < 4.0 :
    print("A nota da Primeira Prova foi: ", a14)
    print("A nota da Segunda Prova foi: ", b14)
    print("A Média final é: ", c14,"Conceito: E")
    print("Aluno REPROVADO")
elif c14 < 6.0 :
    print("A nota da Primeira Prova foi: ", a14)
    print("A nota da Segunda Prova foi: ", b14)
    print("A Média final é: ", c14,"Conceito: D")
    print("Aluno REPROVADO")
elif c14 < 7.5 :
    print("A nota da Primeira Prova foi: ", a14)
    print("A nota da Segunda Prova foi: ", b14)
    print("A Média final é: ", c14,"Conceito: C")
    print("Aluno APROVADO")
elif c14 < 9.0 :
    print("A nota da Primeira Prova foi: ", a14)
    print("A nota da Segunda Prova foi: ", b14)
    print("A Média final é: ", c14,"Conceito: B")
    print("Aluno APROVADO")
elif c14 < 10.0 :
    print("A nota da Primeira Prova foi: ", a14)
    print("A nota da Segunda Prova foi: ", b14)
    print("A Média final é: ", c14,"Conceito: A")
    print("Aluno APROVADO")


#15 -  Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique,
#caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
#Dicas:
#Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#Triângulo Equilátero: três lados iguais;
#Triângulo Isósceles: quaisquer dois lados iguais;
#Triângulo Escaleno: três lados diferentes;

a15 = int(input("Digite um valor: "))
b15 = int(input("Digite um valor: "))
c15 = int(input("Digite um valor: "))

print("")
if (a15+b15 > c15) or (a15+c15 > b15) or (b15+c15 > a15):
    if (a15 == b15) and (a15 == c15):
        print("Os valores formam um triangulo EQUILÁTERO !!! ")
    elif (a15 == b15) or (a15 == c15) or (c15 == b15):
        print("Os Valores formam um triangulo ISÓSCELES !!! ")
    else :
        print("Os Valores formam um triangulo ESCALENO !!!")


# 16 - Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências,
#informando ao usuário nas seguintes situações:
#Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
#Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
#Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
#Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

import math

d16 = "s"

while d16 == "s" :
    a16 = int(input("Digite o Valor de A: "))
    
    if (a16 > 0):
        b16 = int(input("Digite o Valor de B: "))
        c16 = int(input("Digite o Valor de C: "))
        delta = b16*b16 - (4*a16*c16)

        if delta < 0 :
            print("Delta menor que zero")
        elif delta == 0:
            raiz = -b16 / (2*a16)
            print("Delta = 0, raiz: ", raiz)
        else :
            raiz1 = (-b16 + math.sqrt(delta) )/(2*a16)
            raiz2 = (-b16 - math.sqrt(delta) )/(2*a16)
            print("Raizes", raiz1, "e", raiz2)
            d16 = "n"
    else :
        print("Valor de A invalido ")
        d16 = input("Deseja tentar novamente? (S/N) : ")
        d16 = d16.lower()

# 17 - Faça um Programa que peça um número correspondente a um determinado ano e
#em seguida informe se este ano é ou não bissexto.

a17 = int(input("Digite um ano: "))

if a17%4 == 0 :
    if a17%100 != 0:
        print(" O ano digitatado é Bissexto!")
    elif a17%400 == 0:
        print(" O ano digitatado é Bissexto!")
else :
    print("O ano digitado NÃO é Bissexto!")

#18 - Faça um Programa que peça uma data no formato dd/mm/aaaa e
#determine se a mesma é uma data válida.

data = input("digite uma data: ")
dia, mes, ano = data.split("/")

meses_31 = ('01', '03', '05', '07', '08', '10', '12')
data = 'sim'
if (ano > '01') and (mes <= '12')and(mes >= '01') and(dia <= '31') and (dia >= '01'):
    if (data != 'nao') and (mes == 0):
        if (dia < '29'):
            print("True2")
        else:
            print("False2")
    
    elif (data != 'nao') and(mes in meses_31)  and (dia == '31'):
        print("True3")
        if(dia <= '31'):
            print("False3")     
    else :
        data = 'sim'
        
    if (mes =="02"):
        if (int(ano)%400 == 0):
            if (int(dia) <  29):
                data = 'nao'
            else:
                data = 'sim'
        elif (int(ano)%4 == 0) :
            data = 'sim'
        elif (int(ano)%100 == 0) :
            data = 'sim'
        else:
            data = 'nao'
else:
    print("Data Invalida")
    

if data != 'nao' :
    print("Data Valida")
else :
    print("Data invalida para esse ano")


#19 - Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
#Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
#326 = 3 centenas, 2 dezenas e 6 unidades
#12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

a19 = int(input("digite um numero de 1 á 1000: "))

if (a19 >= 1) and (a19 <= 1000):
    numero = a19 % 10
    dezenas = (((a19-numero)%100)/10)
    centenas = ((a19 - dezenas)/100)
    print('O Numero Contém',int(centenas), 'centenas, ' , int(dezenas), 'dezenas e', int(numero), 'unidades')


else :
    print("Numero invalido!")


#20 - Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
#A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
#A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
#A mensagem "Aprovado com Distinção", se a média for igual a 10.


a20 = float(input("Digite a primeira nota: "))
b20 = float(input("Digite a segunda nota:  "))
c20 = float(input("Digite a terceira nota: "))

d20 = (a20+b20+c20)/3

if d20 >= 7 and d20 < 10 :
    print("Aprovado", d20, "Média Final")
elif d20 == 10 :
    print("Aprovado com Distinção!", d20 , "Média Final. Parabéns!")
else :
    print("Reprovado", d20, "Média Final!")

        


#21 - Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas.
#As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais.
#O programa não deve se preocupar com a quantidade de notas existentes na máquina.
#Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
#Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

a21 = float(input("Digite o valor que deseja sacar: R$ "))

if (a21 > 9.99) and (a21 < 600) :
    numero = int(a21 % 10)
    dezenas = int(((a21-numero)%100)/10)
    centenas = int((a21 - dezenas)/100)
    if centenas >= 1:
        print("voce irá sacar: ", centenas, "Notas de R$100")
    if dezenas >= 5 :
        n3 = int((dezenas - 5))
        n4 = int(((dezenas - n3)/5))
        print("voce irá sacar: ", n4, "Notas de R$50")
        if n3 >= 1 :
            print("voce irá sacar: ", n3, "Notas de R$10")
    else :
        n3 = (dezenas)
        if n3 >= 1 :
            print("voce irá sacar: ", n3, "Notas de R$10")
        
    if numero >= 5:
        n1 = int((numero%5))
        n2 = int(((numero - n1)/5))
        print("Voce irá sacar: ", n2, "Notas de R$5")
    else :
        n1 = (numero) 
    if n1 >= 1 :
        print("voce irá sacar: ", n1, "Notas de R$1")
    
if a21 >= 600 :
    print("Não é permitido saque maior que R$ 599,00")
elif a21 <= 9.99 :
    print("Não é permitido saque menor que R$10,00")


# 22 - Faça um Programa que peça um número inteiro e determine se ele é par ou impar.
# Dica: utilize o operador módulo (resto da divisão).

a22 = int(input("Digite um numero: "))

b22 = (a22%2)
if b22 == 1 :
    print("O número: ",a22, "é impar!")
else :
    print("O número: ",a22, "é par!")

#23 - Faça um Programa que peça um número e informe se o número é inteiro ou decimal.
#Dica: utilize uma função de arredondamento.

a23 = float(input("Digite um numero: "))

if a23 == round(a23):
    print("Você digitou um numero Inteiro!")
else:
    print("Você digitou um numero Decimal!")

#24 - Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
#O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
#par ou ímpar;
#positivo ou negativo;
#inteiro ou decimal.

a24 = float(input("Digite um numero: "))
sinal = input("Coloque o Sinal da Operação que deseja fazer(+ - * /): ")
b24 = float(input("Digite outro numero: "))

if sinal == "+" :
    c24 = (a24+b24)
elif sinal == "-" :
    c24 = (a24-b24)
elif sinal == "*" :
    c24 = (a24*b24)
elif sinal == "/" :
    c24 = (a24/b24)
else :
    c24 = ("Sinal Invalido")


if c24 == "Sinal Invalido" :
    print("Sinal invalido!, Tente novamente!")
else: 
    print("O Resultado de ", a24, sinal, b24, "= ", c24)
    d24 = (c24%2)
    if d24 == 1 :
        print("O Resultado é um numero IMPAR!")
    else :
        print("O Resultado é um numero PAR!")

    if c24 < 0 :
        print("O Resultado é um numero NEGATIVO!")
    else :
        print("O Resultado é um numero POSITIVO!")
    e24 = int(c24)
    f24 = e24*10
    g24 = c24*10
    if f24 == g24 :
        print("O Resultado é um numero INTEIRO!")
    else :
        print("O Resultado é um numero DECIMAL!")

#25 - Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#"Já trabalhou com a vítima?"
#O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
#Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
#entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
print("")
print ("INVESTIGAÇÃO DE ASSASSINATO")
print ("")

nome = input("Digite seu nome: ")
print("")
cont1 = 0
p1 = str(input("Você Telefonou para a vitima? :(sim/nao) "))
while cont1 == 0 :
    p1 = p1.lower ()
    if (p1 == "sim") or (p1 == "nao"):
        cont1 += 1
    else :
        p1 = str(input("Resposta Invalida, Tente novamente: Você Telefonou para a vitima? :(sim/nao) "))
    
p2 = str(input("Você Esteve no local do crime? :(sim/nao) "))

cont2 = 0
while cont2 == 0 :
    p2 = p2.lower ()
    if (p2 == "sim") or (p2 == "nao"):
        cont2 += 1
    else :
        p2 = str(input("Resposta Invalida, Tente novamente: Você Esteve no local do crime? :(sim/nao) "))
   
p3 = str(input("Mora perto da vitima? :(sim/nao) "))
cont3 = 0
while cont3 == 0 :
    p3 = p3.lower ()
    if (p3 == "sim") or (p3 == "nao"):
        cont3 += 1
    else :
        p3 = str(input("Resposta Invalida, Tente novamente: Mora perto da vitima? :(sim/nao) "))
        
p4 = str(input("Devia para a vitima? :(sim/nao) "))
cont4 = 0
while cont4 == 0 :
    p4 = p4.lower ()
    if (p4 == "sim") or (p4 == "nao"):
        cont4 += 1
    else :
        p4 = str(input("Resposta Invalida, Tente novamente: Devia para a vitima? :(sim/nao) "))

p5 = str(input("Trabalhou com a vítima? :(sim/nao) "))        
cont5 = 0
while cont5 == 0 :
    p5 = p5.lower ()
    if (p5 == "sim") or (p5 == "nao"):
        cont5 += 1
    else :    
        p5 = str(input("Resposta Invalida, Tente novamente: Trabalhou com a vítima? :(sim/nao) "))

resposta = 0  
if p1 == "sim" :
    resposta =+ 1
if p2 == "sim" :
    resposta += 1
if p3 == "sim" :
    resposta += 1

if p4 == "sim" :
    resposta += 1
if p5 == "sim" :
    resposta += 1

if resposta == 5 :
    print(nome, "é o Assassino!")
elif resposta < 5 and resposta > 2 :
    print(nome, "é Cumplice do Assassinato")
elif resposta == 2 :
    print(nome, "é suspeita do crime")
else :
    print(nome, "é inocente")


# 26 - Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool:  até 20 litros, desconto de 3% por litro, acima de 20 litros, desconto de 5% por litro
# Gasolina: até 20 litros, desconto de 4% por litro, acima de 20 litros, desconto de 6% por litro
#Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina),
#calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

com = str(input("Qual tipo de combustivel deseja utilizar (A- alcool / G - gasolina): "))
lit = float(input("Quantos litros deseja abastecer? : "))
com = com.upper ()
alcool = 1.90
gasolina = 2.50

if com == "A" :
    if lit <= 20 :
        desc = ((lit*1.90)*3/100)
        total = (lit*1.90) - desc
        com = "Alcool"
    else :
        desc = ((lit*1.90)*5/100)
        total = (lit*1.90) - desc
        com = "Alcool"
elif com == "G" :        
    if lit <= 20 :
        desc = ((lit*1.90)*4/100)
        total = (lit*1.90) - desc
        com = "Gasolina"
    else :
        desc = ((lit*1.90)*6/100)
        total = (lit*1.90) - desc
        com = "Gasolina"
else :
    print ("Combustivel invalido, refaça o processo")


print("Voce abasteceu: ", com)
print("a quantidade de: ", lit)
print("o valor a ser pago já com desconto é de : R$%.2f"% total)

input ("")

#27 - Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                      Até 5 Kg           Acima de 5 Kg
#Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra
# ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total.
# Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade
# (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

print("Seja Bem vindo a Quitanda Quintandeira")
print("")
print("Nossos Produtos são: Morango e Maçã ")
print("")
cont = "sim"
t = 0
q = 0
x = 0
while cont == "sim" :
    p = input("Digite o produto escolhido: ")
    q = float(input("Digite a quantidade em KG: "))
    p = p.lower()
    if p == "morango" :
        if q < 5 :
            t = (2.50*q)+t
        else :
            t = (2.20*q)+t
    if p == "maca" :
        if q < 5 :
            t = (1.80*q)+t
        else :
            t = (1.50*q)+t    
    cont = input("deseja comprar mais alguma coisa?(sim/não)")
    cont = cont.lower()
    x = q + x

if x > 8 :
    des = (t*10)/100
    tot = t-des
elif t > 25 :
    des = (t*10)/100
    tot = t-des
else :
    tot = t
    

print("o valor total deu: R$",tot)

input("")




#28 -O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                     Até 5 Kg           Acima de 5 Kg
#File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
#Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
#Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
#Para atender a todos os clientes, cada cliente poderá levar
#apenas um dos tipos de carne da promoção, porém não há limites
#para a quantidade de carne por cliente. Se compra for feita no cartão
#Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra.
#Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e
#gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne,
#preço total, tipo de pagamento, valor do desconto e valor a pagar.

print("Bem Vindo ao Hipermercado TABAJARA".center(80))
print("")
print("Tabela de Preço: ".center(80))
print("")
print("Até 5kg".center(42), "Acima de 5kg".center(1))
print("")
print("File Duplo:", "R$ 4.90kg".center(18), "R$ 5.80kg".center(35))
print("Alcatra:   ", "R$ 5.90kg".center(18), "R$ 6.80kg".center(35))
print("Picanha:   ", "R$ 6.90kg".center(18), "R$ 7.80kg".center(35))
print("")
print("Valores Promocionais, só é permitido a compra de 1 produto por cliente")

p = input("Digite o produto escolhido: ")
p = p.upper()
q = float(input("Digite a quantidade desejada: "))

if p == "FILE DUPLO" :
    if q < 5 :
        t = q*4.90
    else :
        t = q*5.80
if p == "ALCATRA" :
    if q < 5 :
        t = q*5.90
    else :
        t = q*6.80
if p == "PICANHA" :
    if q < 5 :
        t = q*6.90
    else :
        t = q*7.80

f = input("Pagamento com o cartão Tabajara?: ")
f = f.lower()
if f == "sim" :
    des = (t*5)/100
    pag = t-des
    f = ("Cartão Tabajara")
else :
    des = 0
    pag = t-des
    f = ("Outros")

t = (f"{t:6.2f}")
des = (f"{des:6.2f}")
pag = (f"{pag:6.2f}")
q = (f"{q:3.3f}")

print("")
print("Cumpom Fiscal".center(40))
print("")
print("Produto", "Quantidade".center(20))
print(p, str(q).center(20),"kg")
print("")
print("Forma de Pagamento: ", f.center(20))
print("")

print("Valor:      ", "R$: ",str(t).center(20))
print("Desconto:   ", "R$: ",str(des).center(20))
print("Valor Total:", "R$: ",str(pag).center(20))
print("")
print("O Hipemercado TABAJARA agradece a preferencia")




    


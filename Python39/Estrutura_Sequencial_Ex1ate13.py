# 1 - Faça um Programa que mostre a mensagem "Alo mundo" na tela.
print("Exercicio 1")
print("Alo Mundo")

# 2 - Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
print("Exercicio 2")
numero = input("favor digite um numero : ")
print("o numero informado é: ", numero)

# 3 - Faça um Programa que peça dois números e imprima a soma.
print("Exercicio 3")
n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
print("O Resultado da soma dos dois numeros é: ", n1+n2)

# 4 - Faça um Programa que peça as 4 notas bimestrais e mostre a média.
print("Exercicio 4")
nota1 = int(input("Digite a Nota do Primeiro Bimestre: "))
nota2 = int(input("Digite a Nota do Segundo Bimestre: "))
nota3 = int(input("Digite a Nota do Terceiro Bimestre: "))
nota4 = int(input("Digite a Nota do Quarto Bimestre: "))
print("A sua média anual é de: ", (nota1+nota2+nota3+nota4)/4)

# 5 - Faça um Programa que converta metros para centímetros.
print("Exercicio 5")
metro = float(input("digite o tamanho desejado em metros: "))
print("O tamanho convertido é de: ",(metro*100), "centimetros")

# 6 - Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
import math
print("Exercicio 6")
raio = float(input("digite o valor do raio do círculo: "))
print(f"a área desse circulo é de: {math.pi *raio**2:6.2f}")
          
# 7 - Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
print("Exercicio 7")
base = int(input("Digite o tamanho da base do quadrado: "))
altura = int(input("Digite o tamanho da altura do quadrado: "))
print("o tamanho da área do seu quadrado é de ", (base*altura), "já o dobro do seu quadrado é de: ", ((base*altura)*2))

# 8 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
print("Exercicio 8")
sh = float(input("favor digite o valor que voce ganha por hora: "))
ht = int(input("favor digitar a quantidade de horas trabalhadas no mês: "))
salario = sh*ht
print("o seu salario mensal é de: R$%.2f"% salario)

# 9 - Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# 9.A - C = 5 * ((F-32) / 9).
print("Exercicio 9")
f = float(input("Digite a temperatura de hoje em Fahrenheit: "))
c = round(5 * ((f-32) / 9))
print("Hoje está fazendo", c,"Graus Celsius")

# 10 - Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
print("Exercicio 10")
celcius = float(input("Digite a temperatura da água em  Graus Celsius: "))
fah = ((celcius*9)/5)+32
print("a temperatura da água está em %.2f"% fah," Fahrenheit")

# 11 - Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# 11.A - o produto do dobro do primeiro com metade do segundo .
# 11.B - a soma do triplo do primeiro com o terceiro.
# 11.C - o terceiro elevado ao cubo.
print("Exercicio 11")
nu1 = int(input("Digite o primeiro valor: "))
nu2 = int(input("Digite o segundo valor: "))
nu3 = float(input("digite o terceiro valor: "))
a11 = ((nu1*2)*(nu2/2))
b11 = ((nu1*3)+nu3)
c11 = (nu3**3)
print("o produto do dobro do primeiro com metade do segundo, o Resultado é: ",a11)
print("a soma do triplo do primeiro com o terceiro, o Resultado é: ",b11)
print("o terceiro elevado ao cubo, o Resultado é: ",c11)

# 12 - Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
print("Exercicio 12")
h12 = float(input("Digite sua altura: "))
peso = ((72.7*h12)-58)
print("seu peso ideal é de: %.2f"% peso," kg")


# 13 - Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# 13.A - Para homens: (72.7*h) - 58
# 13.B - Para mulheres: (62.1*h) - 44.7
import string
print("Exercicio 13")
h13 = float(input("Digite sua altura: "))
s13 = input("Você é homem ou mulher? (m/h) ")
s13.lower()
if s13 == "m" :
    print(f"Seu peso ídeal é de: {(72.7*h13)-58:6.2f}")
else :
    print(f"Seu peso ídeal é de: {(62.7*h13)-44.7:6.2f}")



 

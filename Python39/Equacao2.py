#Exercicio 1 - Praticando, Efetuar a leitura de três valores (A, B e C) e efetuar o cálculo da equação de segundo grau,
#apresentando as duas raízes, se para os valores informados for possível efetuar o referido cálculo.
#Dica: A fórmula de Báskara é:
import math
a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))

if a==0 :
    print("Valor de A, invalido")
else :
    delta = b*b - (4*a*c)


    if delta < 0 :
        print("Delta menor que zero")
    elif delta == 0:
        raiz = -b / (2*a)
        print("Delta = 0, raiz: ", raiz)
    else :
        raiz1 = (-b + math.sqrt(delta) )/(2*a)
        raiz2 = (-b - math.sqrt(delta) )/(2*a)
        print("Raizes", raiz1, "e", raiz2)


    

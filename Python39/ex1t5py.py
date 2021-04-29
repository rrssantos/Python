#Pedir um número qualquer ao usuário e apresentar o fatorial deste número. Quando o valor 0
#for informado o programa deverá encerrar
import math
a = 1
while a > 0 :
    a =int(input("digite o valor do numero para descobrir o Fatorial: "))
    if a > 0 :
        b =  math.factorial(a)
        print("o faltorial é : ", b)
    else :
        print("Fim")


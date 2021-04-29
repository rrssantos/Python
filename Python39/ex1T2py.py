#Ex: 2 - Entrar com números e imprimir o triplo de cada número. O programa encerra quando o
#usuário informar o número -999 e não deve mostrar o cálculo do triplo de -999.
a = 0
while (a  > -999) :
    a = int(input("Digite um numero: "))
    if (a > - 999) :
        print("o triplo do valor é :", a*3)

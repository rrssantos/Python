#Entrar com números enquanto forem positivos. Quando entrar com número 0 ou algum
#número negativo imprimir quantos números foram digitados.
lista = []
a = 1
while a > 0 :
    a = int(input("digite um numero: "))
    if a > 0 :
        lista.append(a)
else :
    print("os numeros digitados foram: ",(lista))

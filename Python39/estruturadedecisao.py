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


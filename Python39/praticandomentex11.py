numero = [1, 2, 3, 7, 5, 6, 4, 100, 100093, 99999]

resposta = max(numero)

print(resposta)



lista = []
while True:
    i = int(input('Digite um número: '))
    if i < 1: break
    lista.append(i)
for i in reversed(lista):
    print(i)

lis = []
for i in lista :
    if i not in lis :
        lis.append(i)
    lis.sort()

print(lis)



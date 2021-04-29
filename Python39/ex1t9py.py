# 9 - Preparar um programa para gerar os n primeiros termos da
# sequência 1 2 2 4 8 32 256 8192

num = int(input("Digite o numero de termos da sequencia: "))
a = 1
b = aux = 2
print (a, end = " ")
for contador in range(num-1):
    print (aux, end = (" "))
    aux = a*b
    a = b
    b = aux


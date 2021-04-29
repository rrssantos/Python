#Pedir um número qualquer ao usuário e apresentar a soma de todos os seus termos Quando
#o valor 0 for informado o programa deverá encerrar
a = 1  
while a > 0 :
    a = int(input("Digite um numero: "))
    d = a
    if d > 0 :
        b = 0
        lista = [] 
        for b in range(d) :
            d -= 1
            lista.append(d)
        c = sum(lista)
        print(len(lista))
        print("a Soma dos termos é: ", c)


#Apresentar os resultados de uma tabuada de um número qualquer
a = int(input("digite um numero para saber o resultado da tabuada: "))
a0 = a*0
a1 = a*1
a2 = a*2
a3 = a*3
a4 = a*4
a5 = a*5
a6 = a*6
a7 = a*7
a8 = a*8
a9 = a*9
a10 = a*10
print("o resultado de: ",a,"vezes 0 é : ", a0)
print("o resultado de: ",a,"vezes 1 é : ", a1)
print("o resultado de: ",a,"vezes 2 é : ", a2)
print("o resultado de: ",a,"vezes 3 é : ", a3)
print("o resultado de: ",a,"vezes 4 é : ", a4)
print("o resultado de: ",a,"vezes 5 é : ", a5)
print("o resultado de: ",a,"vezes 6 é : ", a6)
print("o resultado de: ",a,"vezes 7 é : ", a7)
print("o resultado de: ",a,"vezes 8 é : ", a8)
print("o resultado de: ",a,"vezes 9 é : ", a9)
print("o resultado de: ",a,"vezes 10 é : ", a10)

b = 0
while (b <= 10):
    c = a*b
    print(a, "x", b, "=", c)
    b += 1
    
    

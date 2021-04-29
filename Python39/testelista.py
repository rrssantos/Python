primos = ['0', 27, 'kady', 18, 2]
print(len(primos))
primos.append(13)
print(len(primos))
print(primos)


for i in range(5) :
    print(i, end= '\t')
    
for contador in range(0,10,2):
    print(contador)

pri = [0, 1, 2, 3, 4, 5]
for cont, elem in enumerate(pri) :
    print(cont,":", elem)

for primos in primos :
    print(primos)

for letras in "python" :
    print (letras, end = '\t')
    
print("")
it = 2
while True :
    if it % 3 == 0 :
        break
    print(it)
    it += 2

for num in range(2,10):
    if (num % 2 == 0):
        print("achou um numero par: ", num, end = " ")
        continue
    print("procurando ....")

impostos = ["MEI", "Simples"]
for impostos in impostos:
    if impostos.startswith("S") :
        continue
    print(impostos)

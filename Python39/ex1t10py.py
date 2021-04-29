#Ler o estado civil de quinze pessoas e mostrar a quantidade de pessoas casadas
pessoas = 1
casado = 0
solteiro = 0
while pessoas <= 15 :
    estado = input("Digite seu estado civil ")
    e = estado.lower()
    if e == "casado" :
        casado = casado + 1
    else :
        solteiro = solteiro + 1
    pessoas += 1
print("Temos o total de: ", casado, "pessoas casadas")    
    

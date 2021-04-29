var_global = input("digite seu nome: ") 
lista1 = []

def see():
    f = "sim"
    v = var_global
    while (f == 'sim'):
        i = int(input("digite sua idade: "))
        s = input("Digite seu sexo (m/f): ")
        c = input("Digite seu CEP: ")
        l = main(i, s)
        t = teste(c)
        print("Olá,", v, "sua idade e sexo é:", l, "Voce mora em: ", t)
        d = input("deseja continuar? ")
        f = d.lower()
        r = lis(v)
        if f == 'sim' :
            v = input("digite seu nome: ")
    
    print(r)
                            
def main(idade, sexo):
    if sexo == 'm':
        sexo = ("Masculino")
    elif sexo == 'f':
        sexo = ("Feminino")
    return (idade, sexo)

def teste(cep, estado='s'):
    if cep == "08290-370" :
        cep = ("Rua Serra de São Domingos")
        estado = ("São Paulo - SP")
    elif cep == "08290-000" :
        cep = ("Itaquera")
        estado = ("São Paulo")
    else :
        cep = ("Não é de São Paulo")
        estado = ("Outro")
    return (cep, estado)

def lis (lista):
    lista1.append(lista)
    return (lista1)
    

see()

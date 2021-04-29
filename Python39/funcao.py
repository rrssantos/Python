var_global = input("digite seu nome: ") 
        
def main(idade, sexo):
    if sexo == 1:
        sexo = ("Masculino")
    else:
        sexo = ("Feminino")
    return (idade, sexo)

def see():
    i = int(input("digite sua idade: "))
    s = int(input("Digite 1 para Masculino e 2 para Feminino: "))
    l = main(i, s)
    print(l)
    print("Olá,", var_global, "sua idade e sexo é:", l)


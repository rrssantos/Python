#Pedir o nome e sexo de uma pessoa. Apresentar no final quantas pessoas são do sexo
#masculino e quantas são do sexo feminino. O programa encerra quando o usuário digitar FIM
#no nome da pessoa.
masc = 0
fem = 0
nome = "nome"
while nome != "fim" :
    nome = input("Digite seu nome, (Para encerrar digite fim): ")
    nome = nome.lower()
    if nome != "fim" :
        sexo = input("Digite seu sexo: ")
        sexo = sexo.lower()
        if sexo == "masculino" or sexo == "m" :
            masc += 1
        elif sexo == "feminino" or sexo == "f" :
            fem += 1
        else :
            print("Sexo Invalido")
print("a quantidade de homens é : ", masc)
print("a quantidade de mulheres é :", fem)



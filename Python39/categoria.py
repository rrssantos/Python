categoria = int(input("digite a categoria:  "))
if categoria < 1 or categoria >5 :
    print("categoria invalida, digite um valor entre 1 e 5")   
else :
    if categoria == 1 :
        preco = 10
    elif categoria == 2 :
        preco = 20
    elif categoria == 3 :
        preco = 30
    elif categoria == 4 :
        preco = 40
    elif categoria == 5:
        preco = 50
    print(f"o preco do produto é R$ {preco:6.2f}")

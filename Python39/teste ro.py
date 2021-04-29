print("Exercicio 13")
h13 = float(input("Digite sua altura: "))
s13 = input("Você é homem ou mulher? (m/h")
if s13 == "m" or s13 == "M" :
    print(f"Se voce for homem seu peso ídeal é de: {(72.7*h13)-58:6.2f}")
else :
    print(f"Se voce for mulher seu peso ídeal é de: {(62.7*h13)-44.7:6.2f}")

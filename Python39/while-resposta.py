contador =1
resposta = "sim"
while (contador < 5) and (resposta == "sim" or resposta == "SIM" or resposta == "s" or resposta == "S"):
    x = int(input("digite um valor para X: "))
    r = x*3
    print("o valor de R é : ", r)
    contador += 1
    print(contador)
    resposta = input("deseja continuar ? (sim/nao)")

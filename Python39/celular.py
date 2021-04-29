minutos = int(input( "digite a quantidade de minutos utilizado no mes:  "))

if minutos < 200 :
    preco = 0.20
else :
    if minutos < 400 :
        preco = 0.18
    else :
        preco = 0.15

print (f"voce vai pagar esse mes, R$ {minutos*preco:6.2f}") 

teste

def single(palavra1) :
    import random
    arquivo = open("Palavras", 'r')
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()
    numero = random.randrange(0, len(palavras))
    palavra = palavras[numero].upper()
    
    return(palavra)

def multi(palavra2) :
    import getpass
    palavra = str(getpass.getpass("Digite a palavra secreta)- "))
    palavra = palavra.strip().upper()
    return(palavra)


print('***********')
print('**Bem vindo ao jogo da Forca!**')
print('***********')

qtd = int(input("Digite 1 para SinglePlayer e 2 Para MultiPlayer: "))
        
if (qtd == 1) :
    p = 0
    palavra_secreta = single(p)
    
elif (qtd == 2) :
    p = 0
    palavra_secreta = multi(p)
palavra_secreta.upper()        

 
def contar(letras) :
    con_let = len(palavra_secreta)
    letras_acertadas = []

    con2 = 0
    while (con2 < con_let) :
      letras_acertadas.append("_")
      con2 += 1
      
    print(letras_acertadas)

    return(letras_acertadas)

def jogo ():
    i = 0
    letras_acertadas = contar(i)
    acertou = False
    enforcou = False

    erros = 0
    while (not acertou and not enforcou):
        chute = input("Qual letra?")
        chute = chute.strip().upper()
        if (chute in palavra_secreta):
            posicao = 0
            for letra in palavra_secreta:
                if (chute.upper() == letra.upper()):
                    #print("encontrei a letra{} na posição{}".format(letra,posicao))
                    letras_acertadas[posicao] = letra
                posicao += 1
        else:
            erros += 1
    
        acertou ="_"not in letras_acertadas
        enforcou = erros ==6
        print(letras_acertadas)
        
       
    if (acertou):
        print("\nVocê ganhou :)\n")
    else:
        print("\nVocê perdeu :(\n")


    print("Fim de Jogo")


    input("press enter")






jogo()



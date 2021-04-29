import getpass
import random
arquivo = open("Palavras", 'w')
arquivo.write("melancia\n")
arquivo.write("banana\n")
arquivo.write("jaca\n")
arquivo.write("santos\n")
arquivo.write("saoroque\n")
arquivo.write("cotia\n")
arquivo.close()


print('***********')
print('**Bem vindo ao jogo da Forca!**')
print('***********')

qtd = int(input("Digite 1 para SinglePlayer e 2 Para MultiPlayer: "))

if (qtd == 1) :
  arquivo = open("Palavras", 'r')
  palavras = []
  for linha in arquivo:
    linha = linha.strip()
    palavras.append(linha)
  arquivo.close()
  numero = random.randrange(0, len(palavras))
  palavra_secreta = palavras[numero].upper()
  if ((palavra_secreta == "MELANCIA") or (palavra_secreta == 'BANANA') or (palavra_secreta == 'jaca')):
      print("Dica: é uma fruta")
  elif((palavra_secreta == 'SANTOS') or (palavra_secreta == 'SAOROQUE') or (palavra_secreta == 'COTIA')):
      print("Dica: é uma cidade")
            
elif (qtd == 2) : 
  palavra_secreta = str(getpass.getpass("Digite a palavra secreta)- "))
  palavra_secreta = palavra_secreta.strip().upper()

con_let = len(palavra_secreta)
letras_acertadas = []

con2 = 0
while (con2 < con_let) :
  letras_acertadas.append("_")
  con2 += 1

print(letras_acertadas)

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
        n = (5 - erros)
        print("Voce ainda tem", n, "chances")
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

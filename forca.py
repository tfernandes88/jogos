import random
def jogar():
    print("*********************************")
    print("***Bem vindo no jogo de Forca!***")
    print("*********************************")

    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()

    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper()

    letras_acertadas = ["_" for letras_acertadas in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    #enquanto(True)
    while(not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0 #posicao
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
        #print("")

    if(acertou):
        print("Você ganhou!!")
    else:
        print("Você perdeu!!")

    print("Fim do jogo")

if(__name__ == "__main__"):

    jogar()


import forca
import Adivinhacao

def escolhe_jogo():
    print("**********************************************")
    print("*************Escolha o seu Jogo***************")
    print("**********************************************")


    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual o jogo"))

    if(jogo == 1):
        print("Jogo Forca?")
        forca.jogar()

    elif(jogo == 2):
        print("Jogando Adivinhação")
        Adivinhacao.jogar()
    print("Fim, Acabou-se")

if(__name__ ==  "__main__"):
    escolhe_jogo()

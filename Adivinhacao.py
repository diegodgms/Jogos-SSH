import random

def jogar():
    print("**********************************************")
    print("Olá, Vamos ao jogo de Adivinhação com mudança")
    print("**********************************************")

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1002

    print("Qual nivel de dificuldade?")
    print("(1) Fácil (2)  Médio (3) Difícil")

    nivel = int(input("Defina o nível:  "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 7



    for rodada in range(1, total_de_tentativas  + 1):
        print("Tentativa {} de {}". format(rodada, total_de_tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou: ", chute_str)
        chute = int(chute_str)

        if(chute  < 1 or chute > 100 ):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        # a variável acerto é do tipo bool que é verdadeiro ou falso
        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Voce acertou \o/ e fez {} pontos".format(pontos))
            break
        else:
            if (maior):
                print("Você Errou! Seu chute foi maior que o numero secreto")
            elif(menor):
                print("Você Errou! Seu chute foi menor que o numero secreto")
                pontos_perdidos = abs(numero_secreto - chute)
                pontos = pontos - pontos_perdidos

        print("Fim, Acabou-se")
if(__name__ ==  "__main__"):
    jogar()
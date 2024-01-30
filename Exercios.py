print("Bem a nossa calculadora, a seguir você irá colocar as informações basicas para realizar um calculo")

num1 = float(input("Digite o primeiro numero:  "))
num2 = float(input("Digite o segundo numero:  "))


operacao = input("Digite o tipo de operação (+, - , / , *): ")

if(operacao == "+" ):
    resultado = num2 + num1
    print("Resultado: ", resultado)

elif(operacao == "-"):
    resultado = num1 - num2
    print("Resultado: ", resultado)

elif(operacao == "/"):
    resultado = num1 / num2
    print("Resultado: ", resultado)

elif(operacao == "*"):
    resultado = num1 * num1
    print("Resultado: ", resultado)
else:
    print("opção invalida!!")
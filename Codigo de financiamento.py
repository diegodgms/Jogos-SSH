# Defina o valor inicial do pedágio sem desconto
valor_pedagio = float(input("Digite o valor inicial do pedágio: "))
total_passagens = int(input("Digite o número total de passagens: "))

# Inicialize o contador de passagens
contador_passagens = 0

# Inicialize o acumulador do valor total com desconto
valor_total_com_desconto = 0

while contador_passagens < total_passagens:
    # Calcule o desconto atual com base no número de passagens
    desconto_atual = 0.05 * contador_passagens

    # Calcule o valor do pedágio com o desconto atual
    valor_com_desconto = valor_pedagio - (valor_pedagio * desconto_atual)

    # Acumule o valor com desconto no valor total com desconto
    valor_total_com_desconto += valor_com_desconto
    print(valor_com_desconto)

    # Atualize o contador de passagens
    contador_passagens += 1

# Exiba o valor total com desconto
print(f"O valor total do pedágio com desconto progressivo em {total_passagens} passagens é: R$ {valor_total_com_desconto:.2f}")

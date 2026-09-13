# APRESENTAÇÃO
print("\n--- BEM VINDO A LANCHONETE DO BONITÃO ---")

# ENTRADA NOME DO CLIENTE
nome_cliente = input("Insira o seu nome para que possamos te chamar quando o pedido estiver pronto: ")

# APRESENTAÇÃO DO CARDÁPIO
print(f"Bem vinda(o) {nome_cliente}! A seguir veja os produtos disponíveis no nosso cardápio:")
print("\n--- CARDÁPIO ---")
print("CÓDIGO -- PRODUTO -- PREÇO (R$)")
print(" 100 -- CACHORRO QUENTE -- R$15,00")
print(" 200 -- HAMBÚRGUER      -- R$24,00")
print(" 300 -- BATATA FRITA    -- R$19,00")
print(" 400 -- REFRIGERANTE    -- R$10,00")
print(" 500 -- SUCO NATURAL    -- R$12,00")

# ACUMULADOR DO VALOR TOTAL DE PEDIDOS
total_pedido = 0.0

# LAÇO PRINCIPAL DO ATENDIMENTO
while True: 
    codigo_prod = int(input("Insira aqui o código do produto desejado: "))

    # Preço unitário do produto é zerado sempre que um novo produto é adicionado
    preco_unitario = 0.0

    # Determina o valor do produto de acordo com o código selecionado
    match codigo_prod:
        case 100:
            preco_unitario = 15.00
        case 200:
            preco_unitario = 24.00
        case 300:
            preco_unitario = 19.00
        case 400:
            preco_unitario = 10.00
        case 500:
            preco_unitario = 12.00
        case _: # Caso seja inserido um código inválido
            print("Código inválido! Tente novamente.")
            continue # retorna o sistema para a primeira linha do While True

    # Laço secundário para a escolha de quantidades dos produtos
    while True:
        quant_prod = int(input("Insira aqui a quantidade de produtos desejado: "))
        if quant_prod > 0:
            break
        else:
            print("Erro: Selecione uma quantidade maior que zero!")

    # CÁLCULOS
    total_item = preco_unitario * quant_prod # Calcula o total de cada item
    total_pedido = total_pedido + total_item # Guarda no acumulador o valor total de cada item
    print(f"Adicionado ao carrinho! Subtotal do item: R${total_item:.2f}")

    # Verifica se o cliente deseja mais itens 
    novo_pedido = input("Deseja pedir algo mais? (S/N): ").upper()

    # Caso o cliente não queira acrescentar mais nada quebra o loop
    if novo_pedido == "N" or novo_pedido == "NÃO" or novo_pedido == "NAO":
        break

# CÁLCULO DE DESCONTO
if total_pedido < 50.00:
    desconto = 0
    desconto_aplicado = total_pedido * 0

elif total_pedido >= 50.00 and total_pedido < 100.00:
    desconto = 5
    desconto_aplicado = total_pedido * 0.05
    valor_final = total_pedido - desconto_aplicado

else:
    desconto = 10
    desconto_aplicado = total_pedido * 0.10
    valor_final = total_pedido - desconto_aplicado

# SELEÇÃO DA FORMA DE PAGAMENTO
pagamento = int(input("Insira aqui a forma de pagamento, sendo: 1 - Dinheiro, 2 - Pix ou 3 - Cartão"))

# SAÍDA
print(f"Pedido de {nome_cliente}:")
print(f"O valor total do seu pedido foi de R${total_pedido}.")
print(f"Você recebeu um desconto de {desconto}% na sua compra!")
print(f"O valor do desconto é de R${desconto_aplicado}.")
print(f"O valor final da sua compra é de R${valor_final}.")

match pagamento:
    case 1:
        forma_pagamento = print("Efetue seu pagamento em Dinheiro!")
    case 2:
        forma_pagamento = print("Efetue seu pagamento no PIX!")
    case 3:
        forma_pagamento = print("Efetue seu pagamento no Cartão!")
    case _:
        print("Por favor, selecione uma forma de pagamento válida!")



# Função 1: Responsável apenas por exibir o cardápio na tela
def mostrar_cardapio():
    print("-" * 43)
    print("                CARDÁPIO")
    print("-" * 43)
    print(" CÓDIGO -- PRODUTO         -- PREÇO (R$)")
    print("  100   -- CACHORRO QUENTE -- R$ 15,00")
    print("  200   -- HAMBÚRGUER      -- R$ 24,00")
    print("  300   -- BATATA FRITA    -- R$ 19,00")
    print("  400   -- REFRIGERANTE    -- R$ 10,00")
    print("  500   -- SUCO NATURAL    -- R$ 12,00")
    print("-" * 43)

# Função 2: Recebe o código digitado e devolve o preço unitário
def obter_preco():
    codigo_prod = input("\nInsira aqui o código do produto desejado: ")
        
    match codigo_prod:
        case "100":
            return 15.00
        case "200":
            return 24.00
        case "300":
            return 19.00
        case "400":
            return 10.00
        case "500":
            return 12.00
        case _:
            # Se for digitado um código inválido, é exibido uma mensagem de erro e é chamada a função novamente
            print("Código inválido! Tente novamente.")
            return obter_preco() 

# Função 3: Avalia o total do pedido e devolve o percentual de desconto
def obter_desconto(total_pedido):
    if total_pedido < 50.00:
        return 0
    elif total_pedido >= 50.00 and total_pedido < 100.00:
        return 5
    else:
        return 10

# Função 4: Prende o usuário no laço até escolher uma forma válida e devolve o texto
def obter_pagamento():
    while True:
        pagamento = input("\nForma de pagamento (1 - Dinheiro, 2 - Pix, 3 - Cartão): ")
        match pagamento:
            case "1":
                return "Dinheiro"
            case "2":
                return "PIX"
            case "3":
                return "Cartão"
            case _:
                print("Por favor, selecione uma forma de pagamento válida!")

# Função 5 (Principal): Controla todo o fluxo do sistema chamando as funções acima
def iniciar_atendimento():
    print("\n--- BEM VINDO A LANCHONETE DO BONITÃO ---")
    nome_cliente = input("Insira o seu nome para que possamos te chamar quando o pedido estiver pronto: ")
    
    print(f"\nBem vinda(o) {nome_cliente}! A seguir veja os produtos disponíveis no nosso cardápio:")
    
    mostrar_cardapio()
    
    total_pedido = 0.0
    
    while True: 
        preco_unitario = obter_preco()
            
        while True:
            mostrar_cardapio()

            quant_prod = int(input("Insira aqui a quantidade de produtos desejado: "))
            if quant_prod > 0:
                break
            else:
                print("Erro: Selecione uma quantidade maior que zero!")
                
        total_item = preco_unitario * quant_prod 
        total_pedido = total_pedido + total_item 
        print(f"Adicionado ao carrinho! Subtotal do item: R${total_item:.2f}")
        
        novo_pedido = input("Deseja pedir algo mais? (S/N): ").upper()
        if novo_pedido == "N" or novo_pedido == "NÃO" or novo_pedido == "NAO":
            break
            
    # Chama a função para descobrir a porcentagem de desconto
    desconto = obter_desconto(total_pedido)
    
    desconto_aplicado = total_pedido * desconto / 100
    valor_final = total_pedido - desconto_aplicado
    
    # Chama a função que gerencia a escolha do pagamento
    forma_pagamento = obter_pagamento()
    
    print("\n" + "-" * 43)
    print(f"Pedido de {nome_cliente}:")
    print(f"O valor total do seu pedido foi de R${total_pedido:.2f}.")
    print(f"Você recebeu um desconto de {desconto}% na sua compra!")
    print(f"O valor do desconto é de R${desconto_aplicado:.2f}.")
    print(f"O valor final da sua compra é de R${valor_final:.2f}.")
    print(f"Forma de pagamento escolhida: {forma_pagamento}")
    print("Obrigado pela preferência!")
    print("-" * 43)

# Executa o programa
iniciar_atendimento()
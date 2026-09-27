# Sistema de Atendimento e Pedidos - Lanchonete do Bonitão

## Disciplina
Algoritmos e Programação - Análise e Desenvolvimento de Sistemas (ADS)

## Nome do Estudante
Raquel Nonato Silva

## Breve Descrição do Programa
Este programa em Python foi desenvolvido para automatizar o atendimento de uma pequena lanchonete, substituindo o registro manual por uma solução digital integrada. 
O sistema recebe a identificação do cliente, apresenta um cardápio interativo estruturado com funções, valida códigos e quantidades de produtos, calcula o subtotal acumulado de forma dinâmica, aplica regras progressivas de desconto com base no valor total da compra e gerencia a seleção da forma de pagamento, exibindo um resumo detalhado ao final do atendimento.

## Principais Funcionalidades Implementadas
* **Modularização por Funções (`def`):** Organização do código em blocos independentes e reutilizáveis para exibição de cardápio, tratamento de preços, cálculo de descontos e validação de pagamentos.

* **Cardápio Interativo:** Exibição estruturada com 5 opções de produtos, identificados por códigos, descrições e preços unitários.

* **Acumulador de Pedidos com Laço (`while` e `match-case`):** Capacidade de realizar múltiplos pedidos em um único atendimento, acumulando o valor total sem a necessidade de utilizar estruturas de dados avançadas.

* **Validação Robusta com Recursividade:** Tratamento de entradas inválidas no código do produto, exibindo mensagens de erro e utilizando chamada recursiva para garantir a integridade dos dados inseridos pelo usuário.

* **Descontos Progressivos:** Aplicação automática de descontos (0% para compras abaixo de R$ 50,00; 5% para valores entre R$ 50,00 e R$ 99,99; e 10% para valores iguais ou superiores a R$ 100,00).

* **Gestão de Pagamento:** Validação e registro da forma de pagamento escolhida (Dinheiro, PIX ou Cartão).

## Instruções Necessárias para Executar o Programa
1. Certifique-se de ter o **Python** instalado no seu computador.
2. Acesse o repositório oficial do projeto no GitHub: [https://github.com/raquelnonato97/Sistema-de-Atendimento-e-Pedidos]
3. Baixe ou clone o repositório contendo o arquivo fonte `index.py`.
4. Abra o seu editor de código de preferência (como o **VS Code**) ou o terminal do seu sistema operacional na pasta onde o arquivo está salvo.
5. Execute o programa digitando o seguinte comando no terminal:
   ```bash
   python index.py
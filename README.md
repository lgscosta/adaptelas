# ✨ Pão com Adaptela ✨

## Descrição
Este é um projeto desenvolvido como trabalho final do curso **Adaptelas** e parte do meu aprendizado em Python. Ele consiste em uma aplicação que gerencia um pedido em lanchonete através de um cardápio presente no arquivo produtos.txt.

## Recursos
- **Gerenciamento de Produtos:** O código possui uma classe GerenciadorProdutos que permite o gerenciamento de produtos, incluindo a leitura de produtos de um arquivo, verificação de disponibilidade, atualização de quantidade e cálculo do valor total da compra.

- **Cardápio:** A função imprimir_cardapio exibe o cardápio de produtos disponíveis com seus respectivos preços.

- **Verificação de Disponibilidade:** A função verificar_disponibilidade verifica se um determinado produto está disponível no estoque e se há quantidade suficiente para atender a um pedido específico.

- **Atualização de Quantidade:** A função atualizar_quantidade atualiza a quantidade de um produto após um pedido ser feito, garantindo que o estoque seja mantido atualizado.

- **Cálculo do Valor da Compra:** A função calcular_valor_compra calcula o valor total de um pedido com base nos produtos selecionados e suas quantidades, levando em consideração a disponibilidade e os preços dos produtos.

- **Resumo do Pedido:** A função imprimir_resumo exibe um resumo detalhado do pedido, incluindo os produtos selecionados, suas quantidades e os valores individuais.

## Requisitos do Sistema
- Python 3.6 ou superior instalado no sistema.
- Arquivo de produtos (produtos.txt) contendo o cardápio e os dados dos produtos sem acento e no formato:
```
Produto(string) Quantidade-em-Estoque(int) Preço-Unitário(float)
```

## Instalação
1. Clone este repositório: `git clone https://github.com/lgscosta/adaptelas`
2. O código fornecido não possui dependências externas além da biblioteca padrão do Python. Portanto, não é necessário instalar pacotes adicionais.

## Como Usar
1. Execute o arquivo principal: `python3 poo.py`
2. Siga as instruções exibidas no terminal para interagir com a aplicação.
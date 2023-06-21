##################################################
#                                                #
#         Trabalho Final Curso Adaptelas         #
#           Tema: Pedido na Lanchonete           #
#         Luana Gabriele de Sousa Costa          #
#                   Jun 2023                     #
#                                                #
##################################################

class Produto:
    def __init__(self, nome, quantidade, preco_unitario):
        self.nome = nome
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario

class GerenciadorProdutos:
    def __init__(self, nome_arquivo):
        self.produtos = self.ler_arquivo_produtos(nome_arquivo)

    def ler_arquivo_produtos(self, nome_arquivo):
        produtos = {}
        with open(nome_arquivo, 'r') as arquivo:
            for linha in arquivo:
                dados = linha.strip().split()
                nome = " ".join(dados[:-2])  # Trata nomes compostos
                quantidade = int(dados[-2])
                preco_unitario = float(dados[-1].replace(',', '.'))
                produtos[nome.lower()] = Produto(nome, quantidade, preco_unitario)

        arquivo.close()  # Fechar o arquivo após terminar a leitura
        return produtos

    def imprimir_cardapio(self):
        print("\033[96m--------------------------------------------------\033[97m")
        print("\033[95mCardápio ✨✨\033[97m")
        for produto, dados in self.produtos.items():
            print(f"{produto.capitalize()} - \033[95mR$ {dados.preco_unitario:.2f}\033[97m")

        print("\033[96m--------------------------------------------------\033[97m")

    def verificar_disponibilidade(self, produto, quantidade):
        if produto in self.produtos:
            prod = self.produtos[produto]

            if prod.quantidade == 0:
                print(f"\n\033[91mNão há {produto.capitalize()} disponível no estoque.\033[97m")
                return -1

            if quantidade <= prod.quantidade:
                return prod.preco_unitario
            else:
                print(f"\n\033[91mNão há quantidade suficiente de {produto.capitalize()} disponível. O que deseja fazer?\033[97m")
                bit = input(f"\033[95m1 - Pegar quantidade máxima ({prod.quantidade:d})\n2 - Cancelar\033[97m\nComando: ")

                if bit == '1':
                    return -2
                else:
                    return -1
        else:
            print(f"\033[91mO produto {produto} não está cadastrado.\033[97m")
            return -1
        return None

    def atualizar_quantidade(self, produto, quantidade):
        if produto in self.produtos:
            prod = self.produtos[produto]
            prod.quantidade -= quantidade

    def calcular_valor_compra(self, pedido):
        valor_total = 0.0
        resumo = []  # Lista para armazenar o resumo dos itens selecionados
        for produto, quantidade in pedido.items():
            preco_unitario = self.verificar_disponibilidade(produto, quantidade)

            if preco_unitario == -2:
                if produto in self.produtos:
                    prod = self.produtos[produto]
                    quantidade = prod.quantidade
                    preco_unitario = self.verificar_disponibilidade(produto, prod.quantidade)

            if preco_unitario >= 0:
                valor_item = quantidade * preco_unitario
                valor_total += valor_item
                self.atualizar_quantidade(produto, quantidade)

                # Adiciona o item ao resumo
                resumo.append(f"  {produto.capitalize()} - {quantidade} unidades - R$ {valor_item:.2f}")

        return valor_total, resumo

    def imprimir_resumo(self, resumo):
        print("\033[96m--------------------------------------------------\033[97m")
        print("\033[95mResumo do pedido:\033[97m")
        for item in resumo:
            print(item)
        print("\033[96m--------------------------------------------------\033[97m\n")

    def escrever_arquivo_pedido(self, resumo, total_pago, bit):
        with open("recibo.txt", 'w') as arquivo:
            if(bit == 's'):
                arquivo.write("Resumo do pedido:\n")
                for item in resumo:
                    arquivo.write(item + "\n")
                print("\033[95m______________________________________________________\033[97m\n")
                arquivo.write("\nTotal pago: R$ {:.2f}".format(total_pago))
                print("Arquivo de pedido criado com sucesso!")

        arquivo.close()  # Fechar o arquivo após terminar a leitura


def main():
    # Nome do arquivo de produtos
    nome_arquivo_produtos = 'produtos.txt'

    # Cria uma instância do GerenciadorProdutos
    gerenciador = GerenciadorProdutos(nome_arquivo_produtos)

    print("╭━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╮")
    print("┃                                         ┃")
    print("┃          \033[95mBem-Vinda à Lanchonete       \033[97m  ┃")
    print("┃     \033[95m   ✨✨ Pão com Adaptela ✨✨    \033[97m   ┃")
    print("┃                                         ┃")
    print("╰━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╯")
    # Obtém o pedido do cliente
    pedido = {}
    while True:
        produto = input("\nDigite o comando desejado, ou o item que deseja:\n  \033[95mmenu -> para ver o cardápio\n  sair -> finalizar o pedido\033[97m\nComando: ")
        produto = produto.lower()  # Converter para letras minúsculas

        if produto == 'sair':
            break

        if produto == 'menu':
            gerenciador.imprimir_cardapio()
        else:
            if gerenciador.verificar_disponibilidade(produto, 0) >= 0:
                quantidade = int(input("Digite a quantidade: "))
                pedido[produto] = quantidade

    # Calcula o valor total da compra e verifica a disponibilidade dos produtos
    valor_compra, resumo = gerenciador.calcular_valor_compra(pedido)

    # Exibe o resumo do pedido
    gerenciador.imprimir_resumo(resumo)

    # Exibe o valor total da compra
    print(f"Valor total da compra: \033[95mR${valor_compra:.2f}\033[97m")
    bit = input("\033[95mDeseja imprimir o resumo? (s/n) \033[97m")
    
    gerenciador.escrever_arquivo_pedido(resumo, valor_compra, bit)

    print("\nObrigada pela preferência! \033[95m<3")

if __name__ == "__main__":
    main()
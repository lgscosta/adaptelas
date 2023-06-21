##################################################
#                                                #
#         Trabalho Final Curso Adaptelas         #
#           Tema: Pedido na Lanchonete           #
#         Luana Gabriele de Sousa Costa          #
#                   Jun 2023                     #
#                                                #
##################################################

# Classe de encapsulamento de um produto 
class Produto:
    def __init__(self, nome, quantidade, preco_unitario): # Inicialização
        self.nome = nome 
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario

# Classe de gerenciamento de uma lista de produtos
class GerenciadorProdutos:
    def __init__(self, nome_arquivo): # Inicialização
        self.produtos = self.ler_arquivo_produtos(nome_arquivo) # Chamada da leitura do arquivo

    # Método de leitura e criação de produtos
    def ler_arquivo_produtos(self, nome_arquivo):
        '''TESTAR ARQUIVO VAZIO OU FORMATO ERRADO'''
        produtos = {} # Inicialmente há uma lista vazia de produtos
        with open(nome_arquivo, 'r') as arquivo: # Abertura do arquivo
            for linha in arquivo:
                dados = linha.strip().split() # Lê todos os dados e separa em uma lista
                nome = " ".join(dados[:-2])  # Essa função join vai unir todos os elementos até antes do penúltimo
                quantidade = int(dados[-2]) # Atribui o valor do penúltimo elemento
                preco_unitario = float(dados[-1].replace(',', '.')) # Atribui o valor do último elemento e substitui a vírgula
                '''TESTAR ENTRADA COM .'''
                produtos[nome.lower()] = Produto(nome, quantidade, preco_unitario) # Cria um produto com lower case no nome

        arquivo.close()  # Fecha o arquivo após terminar a leitura
        return produtos

    # Método de impressão do cardápio
    def imprimir_cardapio(self):
        print("\033[96m--------------------------------------------------\033[97m")
        print("\033[95mCardápio ✨✨\033[97m")
        for produto, dados in self.produtos.items():
            # Capitalize faz a primeira letra ser maiúscula
            print(f"{produto.capitalize()} - \033[95mR$ {dados.preco_unitario:.2f}\033[97m") 

        print("\033[96m--------------------------------------------------\033[97m")

    # Método de verificação da disponiblidade de um produto
    def verificar_disponibilidade(self, produto, quantidade):
        if produto in self.produtos: # Verifica o nome do produto
            prod = self.produtos[produto] # Variável auxiliar para armazenar temporariamente o produto de interesse

            if prod.quantidade == 0: # Se não houver nenhuma quantidade disponível do produto
                print(f"\n\033[91mNão há {produto.capitalize()} disponível no estoque.\033[97m")
                return -1

            if quantidade <= prod.quantidade: # Se a quantidade pedida for menor que a de estoque
                return prod.preco_unitario # Retorna o preço
            else:# Se a quantidade pedida for maior que a de estoque
                print(f"\n\033[91mNão há quantidade suficiente de {produto.capitalize()} disponível. O que deseja fazer?\033[97m")
                # Verificação de procedimento
                bit = input(f"\033[95m1 - Pegar quantidade máxima ({prod.quantidade:d})\n2 - Cancelar\033[97m\nComando: ")

                if bit == '1': # Caso especial
                    return -2
                else:
                    return -1
        else: # Se não estiver cadastrado
            print(f"\033[91mO produto {produto} não está cadastrado.\033[97m")
            return -1
        return None

    # Método de atualização da quantidade de cada produto 
    def atualizar_quantidade(self, produto, quantidade):
        if produto in self.produtos: # Verifica o nome do produto
            prod = self.produtos[produto] # Variável auxiliar para armazenar temporariamente o produto de interesse
            prod.quantidade -= quantidade # Reduz a quantidade original com a quantidade retirada

    # Método de cálculo de valor total 
    def calcular_valor_compra(self, pedido):
        valor_total = 0.0 # Inicializa com 0
        resumo = []  # Lista para armazenar o resumo dos itens selecionados

        for produto, quantidade in pedido.items(): # Verifica o nome do produto e quantidade
            preco_unitario = self.verificar_disponibilidade(produto, quantidade) # Verifica disponibilidade

            if preco_unitario == -2: # Caso retorne -2 significa que o pedido foi maior que a quantidade disponível e o cliente optou por pegar a quantidade máxima disponível
                '''TESTAR REDUNDÂNCIA'''
                if produto in self.produtos:
                    prod = self.produtos[produto]
                    quantidade = prod.quantidade
                    preco_unitario = self.verificar_disponibilidade(produto, prod.quantidade) # Retorna o cálculo com a quantidade disponível

            if preco_unitario >= 0: # Caso retorne 0 ou maior significa que não caiu em nenhum caso de erro
                valor_item = quantidade * preco_unitario # Cálcuo do valor gasto no pedido desse item
                valor_total += valor_item # Soma o valor encontrado no valor total
                self.atualizar_quantidade(produto, quantidade) # Atualização da quantidade do produto disponível

                # Adiciona o item ao resumo
                resumo.append(f"  {produto.capitalize()} - {quantidade} unidades - R$ {valor_item:.2f}")

        return valor_total, resumo

    # Método de impressão do resumo no termnial
    def imprimir_resumo(self, resumo):
        print("\033[96m--------------------------------------------------\033[97m")
        print("\033[95mResumo do pedido:\033[97m")
        for item in resumo:
            print(item)
        print("\033[96m--------------------------------------------------\033[97m\n")

    # Método de escrita de arquivo de recibo
    def escrever_arquivo_pedido(self, resumo, total_pago, bit):
        if(bit == 's'): # Se o cliente tiver pedido recibo
            with open("recibo.txt", 'w') as arquivo: # Abre arquivo para escrita
                arquivo.write("Resumo do pedido:\n")
                for item in resumo:
                    arquivo.write(item + "\n") # Escreve item no arquivo
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

    pedido = {} # Inicialmente vazio
    while True: # Enquanto não for parado
        # Recebe o comando:
        produto = input("\nDigite o comando desejado, ou o item que deseja:\n  \033[95mmenu -> para ver o cardápio\n  sair -> finalizar o pedido\033[97m\nComando: ")
        produto = produto.lower()  # Converter para letras minúsculas

        if produto == 'sair': # Finaliza o loop
            break

        if produto == 'menu': # Imprime o menu
            gerenciador.imprimir_cardapio()
        else: # Se não for comando de saída nem impressão
            # Essa chamada verifica se existe quantidade do produto no estoque ou se existe no cardápio (explicar)
            if gerenciador.verificar_disponibilidade(produto, 0) >= 0: # não é código de erro
                quantidade = int(input("Digite a quantidade: "))
                pedido[produto] = quantidade # Atribui a quantidade

    # Calcula o valor total da compra e verifica a disponibilidade dos produtos
    valor_compra, resumo = gerenciador.calcular_valor_compra(pedido)

    # Exibe o resumo do pedido
    gerenciador.imprimir_resumo(resumo)

    # Exibe o valor total da compra
    print(f"Valor total da compra: \033[95mR${valor_compra:.2f}\033[97m")
    bit = input("\033[95mDeseja imprimir o resumo? (s/n) \033[97m")
    
    # Verificação de procedimento
    gerenciador.escrever_arquivo_pedido(resumo, valor_compra, bit)

    print("\nObrigada pela preferência! \033[95m<3")

# Chamada da main
if __name__ == "__main__":
    main()
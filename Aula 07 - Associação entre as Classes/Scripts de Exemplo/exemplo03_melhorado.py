'''
|------------|         |---------------------|        |-------------|
| Produto    |         | Carrinho            |        | Cliente     |
|------------|         |---------------------|        |-------------|
| descricao  |0..*    1| cliente             |1      1| nome        |
| valor      |---------| produtos            |--------|-------------|
|------------|         |---------------------|        |             |
|            |         | adicionar_produto() |        |-------------|
|------------|         | listar_produtos()   |
                       | calcular_total()    |
                       |---------------------|
'''


class Cliente:
    def __init__(self, nome):
        self.nome = nome


class Produto:
    def __init__(self, descricao, valor):
        self.descricao = descricao
        self.valor = valor


class Carrinho:
    def __init__(self, cliente):
        self.cliente = cliente
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def listar_produtos(self):
        for produto in self.produtos:
            print(produto.descricao, produto.valor)

    def calcular_total(self):
        soma = 0
        for produto in self.produtos:
            soma += produto.valor
        return soma


# objeto Cliente
nome = input('Informe o Nome do Cliente: ')
cliente1 = Cliente(nome)                # cria objeto

# objeto Carrinho
carrinho1 = Carrinho(cliente1)          # associa o carrinho1 com cliente1

quantidade = int(input('Quantidade de Produtos que serão cadastrados: '))

# cadastra os produtos
lista = []
for i in range(quantidade):
    desc = input('\nDescrição do Produto: ')
    valor = float(input('Valor do Produto: '))
    produto = Produto(desc, valor)      # cria um produto
    lista.append(produto)

# exibe lista de produtos
print('\nProdutos Disponíveis para Compra:')
i = 1
for produto in lista:
    print(i, produto.descricao, produto.valor)
    i += 1

while True:
    codigo = int(input('Selecione o código do produto (-1 para sair): '))
    if codigo == -1:
        break

    # verifica se código é valido.
    if codigo < 1 or codigo > len(lista):
        print('Código Inválido')
    else:
        # insere produto selecionado no carrinho
        carrinho1.adicionar_produto(lista[codigo-1])
        print('Produto inserido no carrinho!')

# exibe produtos no carrinho
print('\nProdutos no carrinho:')
carrinho1.listar_produtos()

# exibe o total da compra
print('\nTotal da compra:', carrinho1.calcular_total())

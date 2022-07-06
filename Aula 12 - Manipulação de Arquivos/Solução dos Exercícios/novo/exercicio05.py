arquivo = open('arq.txt', 'r', encoding='UTF-8')

ano_atual = int(input('Ano atual: '))

for linha in arquivo:
    lista = linha.split(' ')

    nome = lista[0]
    idade = ano_atual - int(lista[3])

    print(nome, idade)

arquivo.close()

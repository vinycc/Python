
def busca_nome(lista, indice):
    try:
        if indice < len(lista) and indice >= len(lista) * -1:
            return lista[indice]
        else:
            raise IndexError        # gera uma exceção
    except IndexError:
        return "O indice nao existe"


lista = []
for i in range(5):
    nome = input("Digite um nome: ")
    lista.append(nome)

print(lista)

print(busca_nome(lista, -6))

def funcao_1():
    print('Início da função')
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 999]     # indices: 0...9
    try:
        for i in range(15):
            print(lista[i])
    except IndexError:
        print("Acesso a indice inexistente: ", i)
    print('Fim da função')


print('Início do programa')
funcao_1()
print('Fim do programa')

arquivo1 = open('classe.txt', 'r', encoding='UTF-8')
arquivo2 = open('notas.txt', 'r', encoding='UTF-8')

lista_nomes = []
for nome in arquivo1:
    lista_nomes.append(nome.replace('\n', ''))

lista_notas = []
for nota in arquivo2:
    lista_notas.append(nota.replace('\n', ''))

print(lista_nomes)
print(lista_notas)

nome = input('Nome do aluno: ')

if nome in lista_nomes:
    indice = lista_nomes.index(nome)

    notas = lista_notas[indice].split(' ')
    for i in range(len(notas)):
        notas[i] = float(notas[i])

    print('Notas:', notas)

    media = sum(notas) / len(notas)
    print('Média:', round(media, 2))
else:
    print('Aluno não cadastrado')

arquivo1.close()
arquivo2.close()

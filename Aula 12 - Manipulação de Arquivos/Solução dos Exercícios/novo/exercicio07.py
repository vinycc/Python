arquivo1 = open('arquivo1.txt', 'r', encoding='UTF-8')
arquivo2 = open('arquivo2.txt', 'r', encoding='UTF-8')

conteudo1 = arquivo1.read()
conteudo2 = arquivo2.read()

conteudo1 = conteudo1.replace('\n', ' ').split(' ')
conteudo2 = conteudo2.replace('\n', ' ').split(' ')

lista = []
for a in conteudo1:
    for b in conteudo2:
        if a == b and a not in lista:
            lista.append(a)

for p in lista:
    print(p)

arquivo1.close()
arquivo2.close()

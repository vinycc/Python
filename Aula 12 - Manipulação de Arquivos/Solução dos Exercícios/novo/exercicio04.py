arquivo = open('arquivo.txt', 'r')

vogais = 'aeiouAEIOU'
cont = 0

texto = arquivo.read()
for c in texto:
    if c in vogais:
        cont += 1

print("quantidade de vogais: ", cont)

arquivo.close()

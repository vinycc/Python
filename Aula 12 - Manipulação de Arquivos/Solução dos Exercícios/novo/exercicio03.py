arquivo = open('arquivo.txt', 'w')

while True:
    c = input()
    if c == '0':
        break
    arquivo.write(c)

arquivo.close()

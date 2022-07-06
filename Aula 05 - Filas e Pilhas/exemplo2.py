fila = []               # []       cria uma fila vazia
fila.append(2)          # [2]      insere
fila.append(4)          # [2,4]    insere
fila.append(9)          # [2,4,9]  insere
item = fila.pop(0)      # [4,9]    remove e retorna o item
fila.append(5)          # [4,9,5]  insere
primeiro = fila[0]      # 4        retorna primeiro elemento
tamanho = len(fila)     # 3        retorna tamanho da fila

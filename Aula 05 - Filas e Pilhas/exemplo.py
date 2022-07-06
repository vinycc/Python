pilha = []               #           cria uma pilha vazia
pilha.append(2)          # [2]       insere
pilha.append(4)          # [2,4]     insere
pilha.append(9)          # [2,4,9]   insere
pilha.append(7)          # [2,4,9,7] insere
item = pilha.pop()       # [2,4,9]   remove e retorna o item
item = pilha.pop()       # [2,4]     remove e retorna o item
pilha.append(5)          # [2,4,5]   insere
topo = pilha[-1]         # 5         retorna o item do topo
tamanho = len(pilha)     # 3         retorna tamanho da pilha
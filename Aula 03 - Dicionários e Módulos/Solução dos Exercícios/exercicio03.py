'''
Escreva uma função que conta a quantidade de vogais em um texto
e armazena tal quantidade em um dicionário, onde a chave é a vogal
considerada e o valor é a quantidade de vezes que essa vogal aparece no texto.
A função deve receber o texto como entrada, e retornar o dicionário.
'''


def conta_vogais(texto):
    dicionario = {}
    for letra in texto:
        lista_vogais = 'aeiou'
        if letra in lista_vogais:       # verifica se a letra é vogal sd s
            if letra in dicionario:
                dicionario[letra] += 1
            else:
                dicionario[letra] = 1
    return dicionario


texto = 'faculdade de tecnologia impacta'
dicionario = conta_vogais(texto)
print(dicionario)

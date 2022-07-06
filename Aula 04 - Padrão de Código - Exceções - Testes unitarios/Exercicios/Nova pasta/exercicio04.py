alunos = {}
while len(alunos) < 5:
    try:
        ra = int(input('RA: '))
        if len(str(ra)) != 7:
            raise ValueError
        if ra in alunos:
            raise TypeError
    except ValueError:
        print("O RA nao tem 7 digitos")
    except TypeError:
        print("O RA ja esta cadastrado")
    else:
        nome = input('Nome: ')
        alunos[ra] = nome

print(alunos)

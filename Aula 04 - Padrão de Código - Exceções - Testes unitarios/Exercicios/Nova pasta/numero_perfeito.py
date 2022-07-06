def eh_perfeito(numero):            # 28
    if numero == 0:
        return False

    soma = 0
    for i in range(1, numero):      # 1... 27
        if numero % i == 0:
            soma += i

    if soma == numero:
        return True
    else:
        return False

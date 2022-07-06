try:
    x = int(input('Primeiro valor:'))
    y = int(input('Segundo valor:'))
    z = x / y
    print('O resultado da divisão é:', z)
except ZeroDivisionError:
    print("Ocorreu uma divisão por zero")
except ValueError:
    print("O numero informado esta no formato invalido")
except Exception:
    print("Erro inesperado")
else:
    print('Operação realizada com sucesso')
finally:
    print("Obrigado por usar esse sistema")

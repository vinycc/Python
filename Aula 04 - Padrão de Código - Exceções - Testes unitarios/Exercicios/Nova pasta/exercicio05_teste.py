from exercicio05_modulo import converte_para_celsius, converte_para_fahrenheit


try:
    retorno = converte_para_celsius(32)
    assert retorno == 0
    print("CORRETA")
except AssertionError:
    print("ERRO: valor de retorno: ", retorno, "Valor esperado: 0")

try:
    retorno = converte_para_celsius(41)
    assert retorno == 5
    print("CORRETA")
except AssertionError:
    print("ERRO")


try:
    retorno = converte_para_fahrenheit(27)
    assert retorno == 80.6, 'Erro 1'
    retorno = converte_para_fahrenheit(95)
    assert retorno == 203.0, "Erro 2"
    print("CORRETA")
except AssertionError as erro:
    print("ERRO", erro)

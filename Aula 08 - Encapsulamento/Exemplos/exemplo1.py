class Pessoa:
    def __init__(self, nome, idade, cpf, rg):
        # atributos publicos
        self.nome = nome
        self.idade = idade
        # atributos privados
        self.__cpf = cpf
        self.__rg = rg

    # métodos get: retorna o valor de um atributo
    def get_cpf(self):
        return self.__cpf

    def get_rg(self):
        return self.__rg

    # Métodos set: alterar o valor de um atributo
    def set_cpf(self, cpf):
        self.__cpf = cpf

    def set_rg(self, rg):
        self.__rg = rg


pessoa1 = Pessoa("João", 25, "11111111111", "3333333")
pessoa1.idade = 26                      # Altera a idade
pessoa1.set_cpf("22222222")             # Altera cpf
pessoa1.set_rg("999999999")             # Altera RG

print("Nome: ", pessoa1.nome)           # Exibe o nome
print("CPF:", pessoa1.get_cpf())        # Exibe o CPF
print("RG: ", pessoa1.get_rg())         # Exibe o RG

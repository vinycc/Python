class Funcionario:
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.__salario = salario        # atributo privado

    def set_salario(self, salario):
        if salario > 0:
            self.__salario = salario
        else:
            print("Valor invalido")

    def get_salario(self):
        return self.__salario


funcionario1 = Funcionario("Paulo", 30, 2500)
funcionario1.nome = "Paulo Vieira"
funcionario1.idade = 31
funcionario1.set_salario(3000)

funcionario2 = Funcionario("Maria", 25, 2000)
funcionario2.set_salario(3000)

print("Nome: ", funcionario1.nome)
print("Salario: ", funcionario1.get_salario())


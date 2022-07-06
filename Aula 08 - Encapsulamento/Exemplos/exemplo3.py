from getpass import getpass


class ContaBancaria:
    def __init__(self, numero, titular, senha):
        self.numero = numero
        self.titular = titular
        self.__senha = senha
        self.__saldo = 0

    # metodo privado (metodo interno da classe)
    def __validar_senha(self, senha):
        if senha == self.__senha:
            return True
        else:
            print("Erro: senha invalida")
            return False

    def depositar(self, valor, senha):
        if self.__validar_senha(senha) is True:
            self.__saldo += valor

    def sacar(self, valor, senha):
        if self.__validar_senha(senha) is True:
            self.__saldo -= valor

    def consultar_saldo(self):
        return self.__saldo


conta1 = ContaBancaria(1234, "Paulo Vieira", 123)

valor = float(input("Valor para deposito:"))
senha = int(getpass("Informe a senha:"))
conta1.depositar(valor, senha)
print("Saldo: ", conta1.consultar_saldo())

valor = float(input("Valor para saque:"))
senha = int(getpass("Informe a senha:"))
conta1.sacar(valor, senha)
print("Saldo: ", conta1.consultar_saldo())

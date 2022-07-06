class Veiculo:
    def __init__(self, marca, modelo, placa):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa

    def exibir_dados(self):
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Placa:", self.placa)

    def andar(self):
        print("Veiculo ta andando")


class Carro(Veiculo):                   # Carro herda da classe Veiculo
    def __init__(self, marca, modelo, placa, portas):
        super().__init__(marca, modelo, placa)
        self.portas = portas

    def exibir_dados(self):
        super().exibir_dados()
        print("Portas:", self.portas)


class Moto(Veiculo):                    # Moto herda da classe veiculo
    def __init__(self, marca, modelo, placa, cilindrada):
        super().__init__(marca, modelo, placa)
        self.cilindrada = cilindrada

    def exibir_dados(self):
        super().exibir_dados()
        print("Cilindrada:", self.cilindrada)

    def andar(self):
        print("Moto andando")


carro1 = Carro("Honda", "Fit", "AAA-1234", 4)
carro1.exibir_dados()

moto1 = Moto("Honda", "Biz", "BBB-3456", 1000)
moto1.exibir_dados()

moto1.andar()
Veiculo.andar(moto1)

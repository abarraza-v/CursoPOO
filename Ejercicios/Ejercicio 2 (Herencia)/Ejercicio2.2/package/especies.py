from .animal import Animal


class Mamifero(Animal):
    def __init__(self, nombre, sexo, altura, peso, tipo):
        super().__init__(nombre, sexo, altura, peso, tipo)

    def amamantar(self):
        print(f"{self.nombre} está amamantando...")


class Ave(Animal):
    def __init__(self, nombre, sexo, altura, peso, tipo):
        super().__init__(nombre, sexo, altura, peso, tipo)

    def volar(self):
        print(f"{self.nombre} está volando...")

from package import especies


class Murcielago(especies.Mamifero, especies.Ave):
    def __init__(self, nombre, sexo, altura, peso, tipo):
        super().__init__(nombre, sexo, altura, peso, tipo)

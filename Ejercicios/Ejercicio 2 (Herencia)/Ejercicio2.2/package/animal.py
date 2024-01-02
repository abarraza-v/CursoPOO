class Animal:
    def __init__(self, nombre, sexo, altura, peso, tipo):
        self.nombre = nombre
        self.sexo = sexo
        self.altura = altura
        self.peso = peso
        self.tipo = tipo

    def comer(self):
        print(f"{self.nombre} está comiendo")

class Estudiante:
    def __init__(self, nombre, edad, curso):
        self.nombre = nombre
        self.edad = edad
        self.curso = curso

    def estudiar(self):
        print(f"{self.nombre}: Estudiando...")

    def saludar(self):
        print(f"{self.nombre}: Hola Amigo!")

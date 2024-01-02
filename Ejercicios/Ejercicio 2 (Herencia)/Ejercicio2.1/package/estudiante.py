from .persona import Persona


class Estudiante(Persona):
    def __init__(self, nombre, edad, curso):
        super().__init__(nombre, edad)
        self.curso = curso

    def imprimir_curso(self):
        print(f"{self.nombre}: Mi curso es {self.curso}")

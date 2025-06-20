from abc import ABC, abstractmethod

# Cuando una clase hereda de una superclase abstracta, esta la hace firmar una especie de contrato
# que la obliga a implementar los métodos abstractos. Esto fomenta el polimorfismo y nos evita cometer errores.
# Para transformar una clase en abstracta, debe heredar del objeto ABS (Abstract Base Classes).
class Persona(ABC):
    @abstractmethod
    def __init__(self, nombre, apellido, edad, actividad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.actividad = actividad

    @abstractmethod
    def hacer_actividad(self):
        pass

    def presentarse(self):
        print(f"Hola me llamo: {self.nombre} {self.apellido}. Tengo {self.edad} años")


class Estudiante(Persona):
    def __init__(self, nombre, apellido, edad, actividad):
        super().__init__(nombre, apellido, edad, actividad)

    def hacer_actividad(self):
        print(f"Estoy estudiando: {self.actividad}")


class Trabajador(Persona):
    def __init__(self, nombre, apellido, edad, actividad):
        super().__init__(nombre, apellido, edad, actividad)

    def hacer_actividad(self):
        print(f"Estoy trabajando en el rubro de: {self.actividad}")


# Ya que Persona es una clase abstracta, no se puede instanciar.
# Ale = Persona("Alejandro", "Barraza", 8)

Ale = Estudiante("Alejandro", "Barraza", 18, "programación")
Roberto = Trabajador("Roberto", "Barraza", 25, "desarrollo de software")

Ale.hacer_actividad()
Roberto.hacer_actividad()

class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = int(edad)

    def hablar(self):
        print(f"{self.nombre}: Hola, soy una persona")

    def comer(self):
        print(f"{self.nombre}: Comiendo...")


# La clase empleado está heredando atributos y métodos de la clase Persona
class Empleado(Persona):
    def __init__(self, nombre, apellido, edad, trabajo, salario):
        # Con la función super() definimos qué atributos heredará de la clase Persona
        super().__init__(nombre, apellido, edad)
        # Construimos los atributos especiales de la clase empleado
        self.trabajo = trabajo
        self.salario = int(salario)

    def trabajar(self):
        print(f"Trabajando de {self.trabajo}")

    # Ejemplo de polimorfismo, ya que la clase hablar() para la clase Empleado es diferente.
    def hablar(self):
        print("Hola, soy un empleado")


class Estudiante(Persona):
    def __init__(self, nombre, apellido, edad, carrera, promedionotas):
        # Con la función super() definimos qué atributos heredará de la clase Persona
        super().__init__(nombre, apellido, edad)
        # Construimos los atributos especiales de la clase empleado
        self.carrera = carrera
        self.promedionotas = promedionotas

    def estudiar(self):
        print(f"Estudiando ramos de {self.carrera}")

    # Ejemplo de polimorfismo, ya que la clase hablar() para la clase Estudiante es diferente.
    def hablar(self):
        print("Hola, soy un estudiante")


roberto = Empleado("Roberto", "Rodriguez", 35, "Programación", 1000)
alejandro = Estudiante("Alejandro", "Pérez", 25, "Analista Programador", 6.8)

alejandro.comer()

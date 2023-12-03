class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = int(edad)

    def hablar(self):
        print(f"{self.nombre}: Hola, soy una persona")

    def comer(self):
        print(f"{self.nombre}: Comiendo...")


class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad

    def obtener_habilidad(self):
        return f"mi habilidad es: {self.habilidad}"


class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, apellido, edad, habilidad, empresa, salario):
        Persona.__init__(self, nombre, apellido, edad)
        Artista.__init__(self, habilidad)
        self.empresa = empresa
        self.salario = int(salario)

    def hablar(self):
        print(f"{self.nombre}: Hola, soy un empleado artista")

    def obtener_habilidad(self):
        return f"mi habilidad es NADAAAAA"

    # con super() nos aseguramos de llamar al método de la clase padre y no el método de la sub clase
    def presentarse(self):
        print(
            f"Hola, me llamo {self.nombre}, {super().obtener_habilidad()} y soy empleado de la empresa {self.empresa}"
        )


alejandro = EmpleadoArtista(
    "Alejandro", "Martinez", 25, "acróbata", "Circo Du Sulei", 1000000
)

roberto = Artista("volar")

herencia = issubclass(EmpleadoArtista, Artista)
instancia = isinstance(alejandro, EmpleadoArtista)
instanciaroberto = isinstance(roberto, Artista)

print(instanciaroberto)

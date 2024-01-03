# La abstracción es ocultar la complejidad detrás de un sistema.


class Auto:
    def __init__(self):
        self._estado = "apagado"

    def encender(self):
        self._estado = "encendido"
        print("El auto está encendido")

    def apagar(self):
        self._estado = "apagado"

    def conducir(self):
        if self._estado == "apagado":
            self.encender()
        print("Conduciendo el auto")


mi_auto = Auto()

# En este código, el usuario no se preocupa de verificar si el auto encendió o no antes de conducir, simplemente conduce.
# La complejidad del sistema está oculta mediante abstracción.
mi_auto.conducir()

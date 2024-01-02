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
mi_auto.conducir()
mi_auto.conducir()

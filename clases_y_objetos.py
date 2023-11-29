class Celular:
    # Constructor
    def __init__(self, marca, modelo, camara):
        # Definiendo atributos
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

    # Definiendo métodos de la clase
    def llamar(self):
        print(f"Estás haciendo un llamado desde un: {self.modelo}.")

    def cortar(self):
        print(f"Cortaste la llamada desde tu {self.modelo}.")


celular1 = Celular("Samsung", "S23", "48MP")
celular2 = Celular("Apple", "iPhone 15 Pro", "48MP")

celular2.llamar()

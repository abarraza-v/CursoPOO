class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @nombre.deleter
    def nombre(self):
        del self.__nombre


dalto = Persona("Lucas", 25)

# Gracias a python, podemos eliminar
del dalto.nombre

# Settear
dalto.nombre = "Dalto"

# y hacer get con una sintaxis más limpia.
nombre = dalto.nombre


print(nombre)

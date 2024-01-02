class MiClase:
    def __init__(self):
        # Atributo simbolicamente privado pero se puede acceder a el.
        self._atributo_privado = "Valor"
        # Atributo que no se puede acceder a el desde fuera.
        self.__atributo_ultraprivado = "Valor"

    def __metodoprivado(self):
        pass


objeto = MiClase()
print(objeto._atributo_privado)

# ----------------------------------------------
# Este código tirará error ya que no se puede acceder a el mediante un ".":
#   print(objeto.__atributo_ultraprivado)
# ----------------------------------------------


# los Getters y Setters si pueden acceder a atributos ultra privados.
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    def set_edad(self, nueva_edad):
        self.__edad = nueva_edad


dalto = Persona("Dalto", 23)

dalto.set_nombre("Lucas")
dalto.set_edad(24)

print(dalto.get_edad())

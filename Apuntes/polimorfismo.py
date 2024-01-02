# Está el polimorfismo de de función, el polimorfismo de método y el polimorfismo de herencia.
# En python, podemos hacer sin problema que estas clases funcionen diferente sin que hereden de una superclase. sin embargo, esto no es posible en Java.

# Aquí hay un ejemplo de polimorfismo de herencia y polimorfismo de función.


class Animal:
    def sonido(self):
        pass


class Gato(Animal):
    def sonido(self):
        return "Miau"


class Perro(Animal):
    def sonido(self):
        return "Guau"


def hacer_sonido(animal):
    print(animal.sonido())


gato = Gato()
perro = Perro()

hacer_sonido(perro)

print(gato.sonido())

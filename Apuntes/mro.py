class F:
    def hablar(self):
        print("hola desde F")


class A:
    def hablar(self):
        print("hola desde A")


class B(A):
    def hablar(self):
        print("hola desde B")


class C(A):
    def hablar(self):
        print("hola desde C")


class D(B, C):
    pass


d = D()

d.hablar()

# Forzar que un objeto utilize un método de la clase A, pasándole el objeto como parámetro self
# A.hablar(d)

# El método mro (Method Resolution Order) muestra el orden de qué heredará primero el objeto.
print(D.mro())

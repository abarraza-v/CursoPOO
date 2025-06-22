"""
📘 ISP - Interface Segregation Principle (Principio de Segregación de la Interfaz)

Este principio establece que los clientes **no deben verse obligados a depender de interfaces
que no utilizan**. Una clase solo debería implementar los métodos que realmente necesita.

🧠 ¿Qué significa "interfaz" aquí?

En programación orientada a objetos, una **interfaz** representa un contrato de comportamiento: 
una lista de métodos que una clase debe implementar. **No tiene que ver con interfaces gráficas** 
ni con menús, sino con **estructuras de código**.

En Python, como no existe la palabra clave "interface" como en otros lenguajes, una interfaz se modela 
usando una **clase abstracta ("ABC") con métodos abstractos ("@abstractmethod")**. 
Estas clases no pueden instanciarse directamente, y obligan a sus subclases a implementar los métodos definidos.

✅ Ventajas:
- Evita que las clases implementen métodos innecesarios.
- Favorece la cohesión y el código limpio.
- Reduce el acoplamiento entre componentes.
- Facilita la evolución de la base de código sin efectos colaterales.

Imaginemos una jerarquía de animales donde algunos vuelan, otros nadan y otros corren.
Si una sola interfaz contiene los métodos "volar()", "nadar()" y "correr()",
los animales que no puedan realizar una de esas acciones se verán forzados a
implementarla de forma vacía o incorrecta.
"""

"""❌ MAL EJEMPLO ❌ (Viola ISP)"""
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def volar(self):
        pass

    @abstractmethod
    def nadar(self):
        pass

    @abstractmethod
    def correr(self):
        pass

"""
Aquí cualquier subclase debe **obligatoriamente** definir los tres métodos,
aunque no todos los necesite. Por ejemplo, un Perro no vuela: terminaría
con un método "volar()" vacío o con código innecesario, lo que viola ISP.
"""
class Perro(Animal):
    def volar(self): # Método irrelevante
        pass

    def nadar(self):
        print("El perro nada")

    def correr(self):
        print("El perro corre")

"""✅ BUEN EJEMPLO ✅ (Aplica ISP)"""
# Separamos las capacidades en interfaces pequeñas y específicas:
class PuedeVolar(ABC):
    @abstractmethod
    def volar(self):
        pass


class PuedeNadar(ABC):
    @abstractmethod
    def nadar(self):
        pass


class PuedeCorrer(ABC):
    @abstractmethod
    def correr(self):
        pass


# Ahora cada clase implementa solo lo que necesita:
class Perro(PuedeNadar, PuedeCorrer):
    def nadar(self):
        print("El perro nada")

    def correr(self):
        print("El perro corre")


class Pajaro(PuedeVolar, PuedeCorrer):
    def volar(self):
        print("El pájaro vuela")

    def correr(self):
        print("El pájaro corre")


"""
✅ ¿Qué logramos aplicando ISP?
- Las clases implementan solo los métodos que realmente utilizan.
- Evitamos código muerto o métodos vacíos que inducen a error.
- Reducimos el acoplamiento y aumentamos la cohesión de cada clase.
- El sistema es más fácil de mantener y extender sin efectos secundarios.
"""

# Ejecución del ejemplo con ISP
perro1 = Perro()
perro1.nadar()
perro1.correr()

pajarito = Pajaro()
pajarito.volar()
pajarito.correr()
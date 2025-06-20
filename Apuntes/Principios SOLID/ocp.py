"""
📘 OCP - Open/Closed Principle (Principio de Abierto/Cerrado)

Este principio establece que las entidades de software (módulos, funciones, clases)
deben estar **abiertas para la extensión**, pero **cerradas para la modificación**.

🔓 Abiertas para extensión:
Se pueden añadir nuevas funcionalidades al sistema sin modificar el código existente.

🔒 Cerradas para la modificación:
No se debe cambiar el código que ya funciona correctamente para evitar introducir errores.

✅ Beneficios de aplicar OCP:
- Evita romper código ya funcional.
- Facilita el mantenimiento y la escalabilidad.
- Ayuda a cumplir con el principio de responsabilidad única (SRP).
- Favorece el uso de polimorfismo y herencia correctamente.

🎯 Ejemplo práctico: sistema de descuentos para distintos tipos de clientes.
"""

"""❌MAL EJEMPLO❌ (Viola OCP)"""
class Cliente:
    def __init__(self, tipo):
        self.tipo = tipo

def calcular_descuento(cliente):
    if cliente.tipo == "regular":
        return 0.05
    elif cliente.tipo == "premium":
        return 0.10
    elif cliente.tipo == "vip":
        return 0.15
"""
Este diseño **viola el principio OCP**, ya que cada vez que se agrega un nuevo tipo de cliente,
tenemos que **modificar** la función "calcular_descuento", lo que puede romper el código o generar errores.

El código no está preparado para escalar fácilmente con nuevos tipos de descuento.
"""

"""✅BUEN EJEMPLO✅(Aplica OCP)"""
from abc import ABC, abstractmethod

# Definimos una interfaz abstracta que representa una estrategia de descuento.
# Cualquier clase que herede de esta deberá implementar el método obtener_descuento.
class EstrategiaDescuento(ABC):
    @abstractmethod
    def obtener_descuento(self):
        # Método que debe ser implementado por todas las subclases concretas.
        pass

# Clase concreta que implementa la estrategia de descuento para clientes "regulares".
class DescuentoRegular(EstrategiaDescuento):
    def obtener_descuento(self):
        return 0.05

# Clase concreta para clientes "premium".
class DescuentoPremium(EstrategiaDescuento):
    def obtener_descuento(self):
        return 0.10

# Clase concreta para clientes "VIP".
class DescuentoVIP(EstrategiaDescuento):
    def obtener_descuento(self):
        return 0.15

# Clase Cliente que depende de una estrategia de descuento.
# En lugar de calcular el descuento internamente, delega esa responsabilidad
# a un objeto que implemente EstrategiaDescuento.
class Cliente:
    def __init__(self, nombre, estrategia_descuento: EstrategiaDescuento):
        self.nombre = nombre
        self.estrategia_descuento = estrategia_descuento

    def calcular_descuento(self):
        return self.estrategia_descuento.obtener_descuento()
"""
🧠 ¿Qué conseguimos con este diseño?

- Podemos crear nuevos tipos de descuentos sin modificar la clase Cliente → ✅ Cumple OCP.
- El código es más limpio, escalable y desacoplado.
- Usamos el patrón de diseño Estrategia, que permite cambiar el comportamiento
  del descuento sin cambiar la lógica del cliente.
"""

# Ejecución del ejemplo con OCP
cliente1 = Cliente("Ana", DescuentoRegular())
cliente2 = Cliente("Luis", DescuentoVIP())

print(cliente1.calcular_descuento())  # 0.05
print(cliente2.calcular_descuento())  # 0.15

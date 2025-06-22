"""
📘 OCP - Open/Closed Principle (Principio de Abierto/Cerrado)

Este principio indica que las entidades de software (clases, funciones, módulos) deben estar:

🔓 Abiertas para la extensión:  
Puedes añadir nuevas funcionalidades sin modificar el código existente.

🔒 Cerradas para la modificación:  
El código que ya funciona no debe cambiar al agregar nuevos comportamientos.

🧠 ¿Por qué es útil esto?
Porque evita romper funcionalidades existentes.  
Si un componente debe cambiar cada vez que el sistema crece, es frágil y difícil de mantener.

📦 ¿Cómo se logra esto?
Usando polimorfismo, clases abstractas o interfaces (como en el patrón Estrategia).  
Así, en lugar de modificar, simplemente extendemos comportamientos creando nuevas clases.

---
❌ Mal ejemplo (viola OCP)

Tenemos una función que devuelve el descuento de un cliente según su tipo.
Cada vez que agregamos un nuevo tipo de cliente, tenemos que modificar la función:
"""

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
🔴 Problemas:
- Si llega un nuevo tipo de cliente, como "corporativo", hay que volver a tocar esta función.
- Eso rompe OCP: no está cerrada para modificaciones.
- Además, hay acoplamiento entre la lógica del cliente y los tipos disponibles.

---
✅ Buen ejemplo (aplica OCP correctamente)

Creamos una abstracción que representa el comportamiento de descuento, y cada nuevo tipo de descuento se representa como una nueva clase:
"""

from abc import ABC, abstractmethod

# Interfaz (clase abstracta) que representa una estrategia de descuento
class EstrategiaDescuento(ABC):
    @abstractmethod
    def obtener_descuento(self):
        pass

# Implementaciones concretas de la estrategia
class DescuentoRegular(EstrategiaDescuento):
    def obtener_descuento(self):
        return 0.05

class DescuentoPremium(EstrategiaDescuento):
    def obtener_descuento(self):
        return 0.10

class DescuentoVIP(EstrategiaDescuento):
    def obtener_descuento(self):
        return 0.15

# Cliente depende de la abstracción, no de los detalles
class Cliente:
    def __init__(self, nombre, estrategia_descuento: EstrategiaDescuento):
        self.nombre = nombre
        self.estrategia_descuento = estrategia_descuento

    def calcular_descuento(self):
        return self.estrategia_descuento.obtener_descuento()

"""
🧠 ¿Qué logramos con este diseño?

✅ Podemos agregar nuevos tipos de descuento sin modificar ninguna clase existente.
✅ Cliente no necesita saber nada sobre tipos de descuento, solo usa una estrategia.
✅ Aplicamos correctamente el Principio de Abierto/Cerrado.
✅ Aplicamos el patrón de diseño Estrategia, que permite cambiar el comportamiento de forma flexible.
✅ Código limpio, escalable y mantenible.

---

📌 Aclaraciones importantes sobre OCP

⚠️ OCP no significa que "no se puede cambiar ni una sola línea de código".
Significa que las partes del sistema que ya están funcionando correctamente (en especial las de alto nivel o lógica de negocio) no deberían modificarse innecesariamente al agregar nuevos comportamientos.

🔧 Por otro lado, sí hay clases que están diseñadas para cambiar:  
Son las clases de bajo nivel o de infraestructura (por ejemplo, nuevas implementaciones de estrategias, servicios externos, adaptadores, etc.).

✍️ Es completamente válido (y esperado) crear nuevas clases o modificar clases de bajo nivel cuando agregamos funcionalidades.  
Lo importante es que no tengamos que tocar el núcleo del sistema o romper partes que ya estaban funcionando.

---
💡 Ejemplo 1 — Crear una clase nueva (extensión sin modificación)

Creamos una nueva estrategia de descuento sin tocar la clase Cliente ni las clases existentes:
"""

class DescuentoCorporativo(EstrategiaDescuento):
    def obtener_descuento(self):
        return 0.20

cliente3 = Cliente("Empresa S.A.", DescuentoCorporativo())
print(cliente3.calcular_descuento())  # 0.20

"""
✅ No modificamos nada existente.
✅ Solo añadimos una clase nueva → ✔️ Cumple OCP.

---

💡 Ejemplo 2 — Modificar una clase de bajo nivel (sin violar OCP)

Supongamos que queremos cambiar la lógica de descuento para clientes VIP:
"""

class DescuentoVIP(EstrategiaDescuento):
    def obtener_descuento(self):
        # Antes era 0.15 — ahora aplicamos una nueva política comercial
        return 0.18

"""
✅ Estamos modificando una clase de bajo nivel (una implementación concreta).
✅ No modificamos la clase Cliente ni ninguna parte de la lógica general del sistema.
✅ Esto no viola OCP porque DescuentoVIP es un componente diseñado para ser flexible y evolucionar.

🎯 En resumen:
- Las clases de alto nivel (como Cliente) deben estar cerradas a cambios innecesarios.
- Las clases de bajo nivel (como DescuentoVIP) sí pueden modificarse, porque forman parte del sistema extensible.
- Lo importante es mantener el código desacoplado y predecible: que las decisiones de negocio se puedan adaptar sin romper otras piezas.
"""

"""
📘 SRP - Single Responsibility Principle (Principio de Responsabilidad Única)

Este principio establece que cada clase debe tener una única responsabilidad o razón de cambio.
En otras palabras, una clase debe encargarse de una sola cosa.

Si una clase tiene múltiples responsabilidades, 
entonces puede necesitar modificarse por diferentes razones,
lo que la hace más difícil de mantener, probar y extender.

✅ Ventajas:
- Facilita el mantenimiento.
- Mejora la legibilidad del código.
- Hace que los cambios futuros sean más seguros y predecibles.
- Favorece la reutilización y las pruebas unitarias de componentes aislados.

🔧 Ejemplo conceptual:
Si quisiéramos simular un auto virtual, no sería correcto que una sola clase se encargue de mover el auto 
y calcular el combustible. Cada responsabilidad debería estar separada en clases diferentes.
"""

"""❌MAL EJEMPLO❌ (Viola SRP)"""
class Auto:
    def __init__(self):
        self.posicion = 0
        self.combustible = 100

    def mover(self, distancia):
        COMBUSTIBLE_NECESARIO = distancia / 2
        if self.combustible >= COMBUSTIBLE_NECESARIO:
            self.posicion += distancia
            self.combustible -= COMBUSTIBLE_NECESARIO

            print(f"El auto avanzó {distancia} km.")
"""
❌ Esta clase tiene dos responsabilidades:
1. Controlar el movimiento del auto.
2. Gestionar el nivel de combustible.

Esto significa que, si en el futuro quisiéramos modificar la lógica del movimiento 
(por ejemplo, cómo se calcula la distancia), tendríamos que editar esta clase.
Lo mismo ocurriría si cambiamos cómo se gestiona el combustible.

Cada uno de esos cambios responde a razones distintas, lo que viola el SRP, 
ya que la clase tendría múltiples motivos para cambiar.
"""

"""✅Buen ejemplo✅ (Aplica SRP)"""
# Dividimos las responsabilidades en dos clases:
class TanqueDeCombustible():
    def __init__(self):
        self._combustible = 100

    def agregar_combustible(self, cantidad_que_agregar):
        self._combustible += cantidad_que_agregar

    def restar_combustible(self, cantidad_a_restar):
        self._combustible -= cantidad_a_restar

    @property
    def combustible(self):
        return self._combustible
    

class Auto():
    def __init__(self, tanque_combustible: TanqueDeCombustible):
        self.posicion = 0
        self.tanque_combustible = tanque_combustible
    
    def mover(self, distancia):
        combustible_disponible = int(self.tanque_combustible.combustible)

        COMBUSTIBLE_NECESARIO = int(distancia / 2)
        if combustible_disponible >= COMBUSTIBLE_NECESARIO:
            self.posicion += distancia
            self.tanque_combustible.restar_combustible(COMBUSTIBLE_NECESARIO)
            print(f"El auto avanzó {distancia} km.")
        else:
            print(
                "No hay combustible suficiente.\n"
                f"Combustible restante: {combustible_disponible}\n"
                f"Combustible necesario: {COMBUSTIBLE_NECESARIO}"
                )
"""
✅ ¿Qué logramos?
- "TanqueDeCombustible" se encarga exclusivamente del combustible.
- "Auto" se encarga exclusivamente del movimiento.
- Cada clase tiene una sola razón para cambiar (¡cumple SRP!).
- Podemos modificar o reemplazar una lógica sin afectar a la otra.
"""

# Ejecución del ejemplo con SRP
tanque_combustible = TanqueDeCombustible()
autito = Auto(tanque_combustible)

autito.mover(100)
autito.mover(50)
autito.mover(50)
autito.mover(30)
    

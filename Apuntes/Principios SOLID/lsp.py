"""
📘 LSP - Liskov Substitution Principle (Principio de Sustitución de Liskov)

Este principio establece que las subclases deben poder sustituir a sus clases padre
**sin alterar el comportamiento esperado del programa**.

En otras palabras:
Si una clase B hereda de una clase A, entonces **podemos usar B en cualquier lugar donde se use A, sin romper nada**.

✅ Ventajas:
- Favorece la herencia bien aplicada.
- Evita errores de comportamiento cuando las jerarquías crecen.
- Permite escribir código más robusto y polimórfico.

🧠 Ejemplo conceptual:
Supongamos que queremos modelar aves. Algunas aves pueden volar, pero otras no.  
Si hacemos que todas las aves hereden de una clase "Ave" con el método "volar()", 
corremos el riesgo de que una subclase represente un ave que **no puede volar**, 
como un pingüino, lo que **rompe la lógica esperada**.
"""

"""❌Mal ejemplo❌ (Viola LSP)"""
class Ave:
    def volar(self):
        print("Estoy volando")

"""
En este diseño, todas las aves heredan un método 'volar()',
asumiendo que todas pueden volar. Sin embargo, si creamos una subclase como 'Pinguino',
estaremos violando el Principio de Sustitución de Liskov (LSP), porque un pingüino no puede volar.

Esto significa que, al sustituir una instancia de 'Ave' por una de 'Pinguino',
el comportamiento del programa se vuelve incorrecto o inconsistente.
"""
class Pinguino(Ave):
    pass

"""✅Buen ejemplo✅ (Aplica LSP)"""
class Ave:
    pass


class AveVoladora(Ave):
    def volar(self):
        print("Estoy volando")


class AveNoVoladora(Ave):
    pass


class Pinguino(AveNoVoladora):
    pass

"""
Ahora Pinguino hereda de AveNoVoladora, y ya no tiene un método que no le corresponde.
Esto permite sustituir correctamente subclases sin romper la lógica del programa, 
cumpliendo con el principio de sustitución de Liskov.

✅ ¿Qué logramos aplicando LSP?
- Evitamos que una subclase (Pinguino) herede comportamientos que no le corresponden.
- Separamos correctamente a las aves según su capacidad de volar, creando jerarquías coherentes.
- Podemos sustituir cualquier subclase por su clase padre sin romper el comportamiento del programa.
- Mejoramos la legibilidad, mantenibilidad y coherencia del diseño orientado a objetos.
- Respetamos el principio LSP al evitar que se invoquen métodos inadecuados en ciertas subclases.
"""
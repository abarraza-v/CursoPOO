class Persona:
    # Método especial para construir un objeto
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # Con este método especial definimos cómo se va a mostrar cuando quieran utilizar al objeto como cadena de texto.
    def __str__(self):
        return f"Persona(nombre={self.nombre},edad={self.edad})"

    # Con este método especial definimos la representación del objeto
    def __repr__(self):
        return f'Persona("{self.nombre}",{self.edad})'

    # Con este método especial definimos como se comportará el objeto cuando es sumado.
    def __add__(self, otro):
        nuevo_valor = self.edad + otro.edad
        nuevo_nombre = self.nombre + otro.nombre
        return Persona(nuevo_nombre, nuevo_valor)


ale = Persona("Alejandro", 18)
roberto = Persona("Roberto", 20)
maria = Persona("Maria", 22)

nueva_persona = ale + roberto + maria
print(nueva_persona)

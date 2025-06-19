import os
from utilidades.menu import crear_menu


class Personaje:
    def __init__(self, nombre, fuerza, velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad

    def __add__(self, otro_pj):
        nuevo_nombre = f"{self.nombre}-{otro_pj.nombre}"
        nueva_fuerza = (self.fuerza + otro_pj.fuerza)*1.5
        nueva_velocidad = (self.velocidad + otro_pj.velocidad)*1.5
        return Personaje(nuevo_nombre, nueva_fuerza, nueva_velocidad)
    
    def __repr__(self):
        return f'Personaje(nombre="{self.nombre}", fuerza="{self.fuerza}", velocidad="{self.velocidad}")'
    
    def __str__(self):
        return (
            f"{"=" * 30}\n"
            f"Nombre: {self.nombre}\n" 
            f"Fuerza: {self.fuerza}\n"
            f"Velocidad: {self.velocidad}\n"
            f"{"=" * 30}\n"
        )

lista_personajes = []

def main():
    menu_principal()


def menu_principal():
    while True:
        os.system('cls')
        print(crear_menu(
            "JUEGO DE FUSIONES", {
            "1": "Crear Personaje", 
            "2": "Fusionar Personajes", 
            "3": "Mostrar Personajes", 
            "0": "Salir"
            }))
        
        opcion = input("INGRESE UNA OPCIÓN: ").strip()

        if opcion == "1":
            while True:
                os.system("cls")
                crear_personaje()
                if input("Para volver al menú principal ingresa 'Q'. Presiona Enter para continuar: ").lower().strip() == "q":
                    break
        elif opcion == "2":
            while True:
                os.system("cls")
                fusionar_personajes()
                if input("Para volver al menú principal ingresa 'Q'. Presiona Enter para continuar: ").lower().strip() == "q":
                    break
        elif opcion == "3":
            while True:
                os.system("cls")
                mostrar_personajes()
                if input("Para volver al menú principal ingresa 'Q'. Presiona Enter para continuar: ").lower().strip() == "q":
                    break
        elif opcion == "0":
            break
        else:
            input("Opción inválida")


def agregar_personaje_a_lista(personaje):
    global lista_personajes
    lista_personajes.append(personaje)


def crear_personaje():
    nombre_personaje = input("Ingrese el nombre de su personaje: ").strip().title()
    try:
        fuerza_personaje = int(input("Ingrese la fuerza de su personaje (Solo puedes ingresar números enteros): "))
        velocidad_personaje = int(input("Ingrese la velocidad de su personaje (Solo puedes ingresar números enteros): "))
    except ValueError:
        print("Error: Ingrese números enteros.")
    else:
        print("Personaje agregado a la lista!")
        personaje = Personaje(nombre_personaje, fuerza_personaje, velocidad_personaje)
        agregar_personaje_a_lista(personaje)
        

def fusionar_personajes():
    print(crear_menu("FUSIONAR PERSONAJES"))
    mostrar_personajes()
    nombre_personaje_1 = input("Ingrese el nombre de un personaje: ").strip().title()
    nombre_personaje_2 = input("Ingrese un segundo personaje con el cual fusionarlo: ").strip().title()

    personaje1 = buscar_personaje_por_nombre(nombre_personaje_1)
    personaje2 = buscar_personaje_por_nombre(nombre_personaje_2)

    if personaje1 is None or personaje2 is None:
        print("❌ Uno o ambos personajes no existen.")
        return None

    try:
        personaje_fusionado = personaje1 + personaje2
    except Exception as e:
        print(f"Ocurrió un error inesperado durante la fusión: {e}")
    else:
        agregar_personaje_a_lista(personaje_fusionado)
        print(f"Tu nueva fusión es:\n{personaje_fusionado}")
        return personaje_fusionado


def buscar_personaje_por_nombre(nombre_personaje):
    global lista_personajes
    for personaje in lista_personajes:
        if personaje.nombre == nombre_personaje:
            return personaje
    return None


def mostrar_personajes():
    global lista_personajes
    print(crear_menu("LISTA DE PERSONAJES"))
    for personaje in lista_personajes:
        print(personaje)

main()
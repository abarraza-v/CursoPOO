from .estudiante import Estudiante


def crear_estudiantes(num):
    estudiantes = dict()
    for i in range(num):
        nombre = input(f"Ingrese el nombre del estudiante número {i+1}  ")
        edad = int(input(f"Ingrese la edad del estudiante número {i+1}  "))
        curso = input(
            f"Ingrese el curso del estudiante número {i+1} (Ej: 1ero Medio, 1ero Básico)  "
        ).lower()

        estudiantes[f"{nombre}"] = Estudiante(nombre, edad, curso)

    return estudiantes


def mostrar_estudiantes(estudiantes):
    print("------- ESTUDIANTES -------")
    for estudiante in estudiantes.values():
        print(
            f"""
            NOMBRE: {estudiante.nombre}
            EDAD: {estudiante.edad}
            CURSO: {estudiante.curso} \n
            --------------------------"""
        )

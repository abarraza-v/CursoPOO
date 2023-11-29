from package.funciones_estudiante import crear_estudiantes, mostrar_estudiantes

estudiantes = crear_estudiantes(2)

mostrar_estudiantes(estudiantes)

while True:
    try:
        nombre_estudiante = input(
            "Ingrese el nombre del estudiante que quiere como personaje  "
        )
        if nombre_estudiante == "salir":
            break

        estudiante = estudiantes[nombre_estudiante]
        break

    except ValueError:
        print("No ingresaste un nombre válido")


while True:
    accion = input(f"Qué acción quieres que haga {estudiante.nombre}  ")
    if accion == "salir":
        break

    try:
        metodo = getattr(estudiante, accion, None)
        if metodo is None and not callable(metodo):
            raise ValueError()
        else:
            metodo()
    except ValueError:
        print(f"{estudiante.nombre} no puede hacer esa acción")

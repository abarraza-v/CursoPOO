# El decorador toma como parámetro la función en sí, luego le añade código a su funcionalidad.
def decorador(funcion):
    def funcion_y_añadidos():
        print("Antes de la ejecución")
        funcion()
        print("Después de la ejecución")

    return funcion_y_añadidos


# def saludo():
#     print("Hola soy Roberto")


# saludo_y_añadidos = decorador(saludo)
# saludo_y_añadidos()


@decorador
def saludo():
    print("Hola soy Roberto")


saludo()

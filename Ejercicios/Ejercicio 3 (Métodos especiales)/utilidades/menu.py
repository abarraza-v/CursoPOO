def crear_menu(titulo, opciones = None):
    """
    Esta función crea un menú en formato string dependiendo de los parámetros entregados.

    Parámetros:
    titulo (string): El título del menú.
    opciones (dict, opcional): Un diccionario con las opciones disponibles en el menú. 
    Si no se proporciona, el valor predeterminado es None.

    Retorna:
    menu (string): Una cadena de texto que contiene el menú listo para imprimir, 
    con el título centrado en 32 caracteres y, si se proporcionan, las opciones incluidas también.
    
    """
    # Se crea el menú con el título centrado.
    menu = "=" * 32 + "\n" + f"{titulo:^32}" + "\n" + "=" * 32
    # Si no se enviaron opciones, el código termina aquí, si no, las integrará al menú.
    if opciones is None:
        menu += "\n"
        return menu
      
    for key, value in opciones.items():
        menu += f"\n     {key}.- {value}       "
    
    menu += "\n"
    return menu
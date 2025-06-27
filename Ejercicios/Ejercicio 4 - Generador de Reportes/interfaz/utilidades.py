def generar_menu_consola(titulo: str, opciones: list = None) -> str:
    """
    Genera un menú de texto con el título centrado y una lista de opciones enumeradas.

    Parámetros:
        titulo (str): Título del menú, centrado en el encabezado.
        opciones (list[str], opcional): Lista de opciones a mostrar en el menú. 
                                         Si se omite, solo se muestra el título.

    Retorna:
        str: Menú formateado como cadena lista para imprimir en consola.
    """
    menu = "=" * 32 + "\n" + f"{titulo:^32}" + "\n" + "=" * 32

    if not opciones:
        return menu + "\n"

    for i, texto_opcion in enumerate(opciones, start=1):
        menu += f"\n  {i}. {texto_opcion}"

    return menu + "\n"
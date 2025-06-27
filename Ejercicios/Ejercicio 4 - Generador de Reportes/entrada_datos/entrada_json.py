from entrada_datos import EntradaDatos
from reportes import DatosReporte
from interfaz.utilidades import generar_menu_consola

class EntradaDatosJSON(EntradaDatos):
    def obtener_datos(self):
        encabezados = input("Ingresa las claves que tendrán sus JSON separados por coma:\n> ").split(",")
        encabezados = [encabezado.strip().capitalize() for encabezado in encabezados]
        filas = []
        print("Ingrese los valores de cada JSON: ")
        while True:
            print(generar_menu_consola("NUEVO JSON"))
            fila = []
            for encabezado in encabezados:
                valor = input(f"{encabezado}: ")
                fila.append(valor)
            filas.append(fila)    

            if "x" == input("Presiona Enter para continuar agregando filas. Ingresa 'x' para terminar: ").lower():
                break
        return DatosReporte(encabezados=encabezados, filas=filas)
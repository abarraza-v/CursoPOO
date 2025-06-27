from entrada_datos import EntradaDatos
from reportes import DatosReporte
from interfaz.utilidades import generar_menu_consola

class EntradaDatosCSV(EntradaDatos):
    def obtener_datos(self):
        encabezados = input("Ingrese encabezados separados por coma:\n> ").split(",")
        encabezados = [encabezado.strip().capitalize() for encabezado in encabezados]
        filas = []
        print("Ingrese los datos de cada fila: ")
        while True:
            print(generar_menu_consola("NUEVA FILA"))
            fila = []
            for encabezado in encabezados:
                valor = input(f"{encabezado}: ")
                fila.append(valor)
            filas.append(fila)    

            if "x" == input("Presiona Enter para continuar agregando filas. Ingresa 'x' para terminar: ").lower():
                break
        return DatosReporte(encabezados=encabezados, filas=filas)
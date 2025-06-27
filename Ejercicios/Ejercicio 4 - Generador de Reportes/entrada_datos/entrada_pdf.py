from entrada_datos import EntradaDatos
from reportes import DatosReporte

class EntradaDatosPDF(EntradaDatos):
    def obtener_datos(self):
        contenido = input("Ingrese el contenido del reporte: ")
        return DatosReporte(contenido=contenido)
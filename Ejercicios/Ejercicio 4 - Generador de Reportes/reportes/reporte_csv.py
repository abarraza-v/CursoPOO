import os
import csv

from reportes import GeneradorReporte, DatosReporte
from notificaciones.base import Notificador

class ReporteCSV(GeneradorReporte):
    def __init__(self, notificador: Notificador):
        self._notificador = notificador
        
    @property
    def notificador(self):
        return self._notificador

    def generar_reporte(self, datos: DatosReporte, carpeta_destino="./Ejercicios/Ejercicio 4 (SOLID)/reportes_generados/reportes_csv", nombre_archivo_a_generar="test"):
        os.makedirs(carpeta_destino, exist_ok=True)
        ruta_completa = os.path.join(carpeta_destino, nombre_archivo_a_generar + ".csv")

        with open(ruta_completa, "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(datos.encabezados)  # Escribe la primera fila (encabezados)
            escritor.writerows(datos.filas)       # Escribe múltiples filas de datos
        self.notificador.notificar_exito(f"✅ ¡Se ha generado el reporte! Reporte guardado en: {ruta_completa}.\nDatos guardados:\n{datos}")        
        return ruta_completa
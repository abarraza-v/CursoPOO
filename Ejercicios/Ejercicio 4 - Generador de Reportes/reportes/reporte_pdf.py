import os
from fpdf import FPDF

from reportes import GeneradorReporte, DatosReporte
from notificaciones.base import Notificador

class ReportePDF(GeneradorReporte):
    def __init__(self, notificador: Notificador):
        self._notificador = notificador

    @property
    def notificador(self):
        return self._notificador
        
    def generar_reporte(self, datos: DatosReporte, carpeta_destino="./Ejercicios/Ejercicio 4 (SOLID)/reportes_generados/reportes_pdf", nombre_archivo_a_generar="test"):
        os.makedirs(carpeta_destino, exist_ok=True)
        ruta_completa = os.path.join(carpeta_destino, nombre_archivo_a_generar + ".pdf")
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        for linea in datos.contenido.split("\n"):
            pdf.cell(0, 10, txt=linea, ln=True)

        pdf.output(ruta_completa)
        self.notificador.notificar_exito(f"✅ ¡Se ha generado el reporte! Reporte guardado en: {ruta_completa}.\nDatos guardados:\n{datos}")        
        return ruta_completa
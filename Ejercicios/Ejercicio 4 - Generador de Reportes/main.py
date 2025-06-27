from interfaz.menu_usuario import MenuUsuario
from interfaz.registro import RegistroTiposReporte
from notificaciones.consola import NotificadorConsola
from reportes.reporte_json import ReporteJSON
from reportes.reporte_pdf import ReportePDF
from reportes.reporte_csv import ReporteCSV
from entrada_datos.entrada_pdf import EntradaDatosPDF
from entrada_datos.entrada_json import EntradaDatosJSON
from entrada_datos.entrada_csv import EntradaDatosCSV

def main():
    notificador_consola = NotificadorConsola()

    registro = RegistroTiposReporte()
    registro.registrar(
        "json",
        "Generar reporte JSON",
        EntradaDatosJSON(),
        ReporteJSON(notificador_consola)
    )

    registro.registrar(
        "pdf",
        "Generar reporte PDF",
        EntradaDatosPDF(),
        ReportePDF(notificador_consola)
    )

    registro.registrar(
        "csv",
        "Generar reporte CSV",
        EntradaDatosCSV(),
        ReporteCSV(notificador_consola)
    )
    
    menu_usuario = MenuUsuario(registro, notificador_consola)

    menu_usuario.mostrar()

if __name__ == "__main__":
    main()
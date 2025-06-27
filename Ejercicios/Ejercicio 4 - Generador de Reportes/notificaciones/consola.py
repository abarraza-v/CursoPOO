from tabulate import tabulate
from notificaciones.base import Notificador

from reportes.datos import DatosReporte

class NotificadorConsola(Notificador):
    def notificar_exito(self, mensaje = "Acción completada exitosamente"):
        print(mensaje)
    
    def mostrar_tabla(self, datos: DatosReporte):
        tabla = tabulate(datos.filas, headers=datos.encabezados, tablefmt="fancy_grid")
        print(tabla)
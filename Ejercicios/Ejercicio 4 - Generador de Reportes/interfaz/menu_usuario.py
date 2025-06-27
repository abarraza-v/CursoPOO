from interfaz.utilidades import generar_menu_consola
from interfaz.registro import RegistroTiposReporte
from notificaciones.base import Notificador

class MenuUsuario:
    def __init__(self, registro: RegistroTiposReporte, notificador: Notificador):
        self._registro = registro
        self._notificador = notificador
        self._acciones = {
            str(i + 1): (tipo, self._menu_generar_reporte)
            for i, tipo in enumerate(registro.generadores.keys())
        }
        self._acciones[str(len(self._acciones) + 1)] = ("salir", self._salir)

    def mostrar(self):
        while True:
            opciones = [
                self._registro.etiquetas_menu[tipo_reporte] if tipo_reporte != "salir" else "Salir"
                for tipo_reporte, _ in self._acciones.values()
            ]
            print(generar_menu_consola("Menú Principal", opciones))
            numero_accion = input("Seleccione una opción: ").strip()
            accion = self._acciones.get(numero_accion)
            if accion:
                accion = self._acciones.get(numero_accion)
                tipo, funcion = accion
                funcion(tipo) if tipo != "salir" else funcion()
            else:
                print("❌ Opción inválida.")

    def _menu_generar_reporte(self, tipo):
        entrada = self._registro.entradas.get(tipo)
        if not entrada:
            print(f"❌ No hay estrategia de entrada de datos para el tipo '{tipo}'.")
            return
        
        datos = entrada.obtener_datos()
        
        generador = self._registro.generadores.get(tipo)
        if generador:
            nombre_archivo = input("Ingrese el nombre del archivo que se generará: ").strip()
            ruta = generador.generar_reporte(datos, nombre_archivo_a_generar=nombre_archivo)
            self._notificador.notificar_exito(f"✅ Reporte generado: {ruta}")
        else:
            print(f"❌ No se encontró generador para '{tipo}'.")
            return
    
    def _salir(self):
        print("👋 Saliendo del programa...")
        exit()
from reportes import GeneradorReporte
from entrada_datos import EntradaDatos

class RegistroTiposReporte:
    def __init__(self):
        self._entradas_por_tipo = {}
        self._generadores_por_tipo = {}
        self._etiquetas_menu = {}

    def registrar(self, tipo: str, etiqueta: str, entrada: EntradaDatos, generador: GeneradorReporte):
        self._entradas_por_tipo[tipo] = entrada
        self._generadores_por_tipo[tipo] = generador
        self._etiquetas_menu[tipo] = etiqueta
    
    @property
    def entradas(self):
        return self._entradas_por_tipo

    @property
    def generadores(self):
        return self._generadores_por_tipo
    
    @property
    def etiquetas_menu(self):
        return self._etiquetas_menu
from tabulate import tabulate

class DatosReporte:
    def __init__(self, encabezados=None, filas=None, contenido=None):
        self._encabezados = encabezados
        self._filas = filas
        self._contenido = contenido
    
    @property
    def encabezados(self):
        return self._encabezados
    
    @property
    def filas(self):
        return self._filas
    
    @property
    def contenido(self):
        return self._contenido
    
    def __str__(self):
        if self._contenido:  # Caso PDF, texto plano
            return self._contenido
        elif self._encabezados and self._filas:
            return tabulate(self._filas, headers=self._encabezados, tablefmt="fancy_grid")
        else:
            return "[Datos vacíos]"
        
    def __repr__(self):
        return (
            f"DatosReporte(encabezados={self._encabezados}," 
            f"filas={len(self._filas) if self._filas else 0}," 
            f"contenido={'Sí' if self._contenido else 'No'})"
        )
    
    def a_dict(self):
        if not self.encabezados or not self.filas:
            return []
        if any(len(fila) != len(self.encabezados) for fila in self.filas):
            raise ValueError("Algunas filas no coinciden con los encabezados")
        return [dict(zip(self.encabezados, fila)) for fila in self.filas]

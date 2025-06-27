from abc import ABC, abstractmethod
from reportes.datos import DatosReporte

class GeneradorReporte(ABC):
    @abstractmethod
    def generar_reporte(self, datos: DatosReporte):
        pass
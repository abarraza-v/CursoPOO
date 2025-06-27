from abc import ABC, abstractmethod

class EntradaDatos(ABC):
    @abstractmethod
    def obtener_datos(self):
        pass
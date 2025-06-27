from abc import ABC, abstractmethod

class Notificador(ABC):
    @abstractmethod
    def notificar_exito(self, mensaje = "Acción completada exitosamente"): 
        pass
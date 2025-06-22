"""
📘 DIP - Dependency Inversion Principle (Principio de Inversión de Dependencias)

Este principio es uno de los pilares del diseño orientado a objetos y dice lo siguiente:

🧩 Las clases que contienen la lógica principal (alto nivel) no deberían depender directamente de clases que hacen tareas técnicas específicas (bajo nivel).  
Ambas deben depender de una abstracción.

🎯 ¿Qué es “alto nivel” y “bajo nivel”?

- Módulo de alto nivel: es el que representa la lógica del negocio, como Notificador, RegistrarUsuario, ProcesarPago, etc.  
  Estas clases describen "qué hace el sistema".

- Módulo de bajo nivel: son los detalles técnicos que ejecutan acciones específicas, como enviar un email, guardar en base de datos, o conectarse a una API.  
  Ejemplos: EmailService, SMSService, FileLogger, etc.

📌 ¿Qué significa que “ambos deben depender de una abstracción”?

Significa que tanto las clases de alto nivel como las de bajo nivel deben trabajar a través de una interfaz común (una abstracción), y no depender directamente entre sí.

Así se logra que el código sea flexible, extensible y fácil de mantener.

---
🧠 ¿Qué es una interfaz en este contexto?

Una interfaz es una especie de contrato que define un conjunto de métodos que una clase debe implementar.

En lenguajes como Java o C# existen como estructuras propias (interface), pero en Python no.  
Sin embargo, podemos lograr el mismo comportamiento usando:

✅ Clases abstractas (heredando de abc.ABC).  
✅ Métodos obligatorios definidos con @abstractmethod.

Esto permite definir una "estructura base" que otras clases deben seguir, sin imponer cómo debe funcionar cada método.

---
❌ Mal ejemplo (viola DIP)

La clase Notificador depende directamente de una clase técnica concreta (EmailService). Si queremos cambiar el canal de notificación, hay que reescribir esta clase:
"""

class EmailService:
    def enviar_email(self, mensaje):
        print(f"Enviando email: {mensaje}")

class Notificador:
    def __init__(self):
        self.servicio = EmailService()  # ← Acoplamiento fuerte

    def notificar(self, mensaje):
        self.servicio.enviar_email(mensaje)

"""
🔴 Problemas:
- Notificador depende de un detalle técnico (EmailService).
- No podemos cambiar el canal de notificación sin modificar Notificador.
- No se puede reutilizar con otras implementaciones como SMSService o WhatsAppService.
- Rompe el principio DIP, porque el módulo de alto nivel está dependiendo del bajo nivel.

---
✅ Buen ejemplo (aplica DIP correctamente)

Creamos una clase abstracta llamada ServicioNotificacion y hacemos que Notificador trabaje con ella, sin importar qué implementación se use:
"""

from abc import ABC, abstractmethod

class ServicioNotificacion(ABC):
    @abstractmethod
    def enviar(self, mensaje: str):
        pass

class EmailService(ServicioNotificacion):
    def enviar(self, mensaje: str):
        print(f"Enviando email: {mensaje}")

class Notificador:
    def __init__(self, servicio: ServicioNotificacion):
        self.servicio = servicio  # ← Ahora depende de una abstracción

    def notificar(self, mensaje):
        self.servicio.enviar(mensaje)

"""
🧠 ¿Qué logramos?

- Ahora Notificador no sabe ni le importa cómo se envía el mensaje.
- Solo necesita un objeto que cumpla con la interfaz ServicioNotificacion.
- Podemos cambiar EmailService por cualquier otra clase que implemente esa interfaz (como SMSService, WhatsAppService, etc.) sin tocar la lógica de Notificador.
- Esto es cumplir DIP: la lógica de negocio y los detalles técnicos están desacoplados.

---
📦 ¿Y cómo esto también ayuda a mantener el código extensible?

Imaginemos que tenemos una función registrar_usuario():

❌ Si Notificador depende internamente de EmailService, entonces registrar_usuario también queda amarrada a ese servicio:

""" 
def registrar_usuario():
    notificador = Notificador()  # usa EmailService internamente
    notificador.notificar("Bienvenido") 
"""

✅ Pero si seguimos DIP, registrar_usuario puede recibir cualquier servicio por fuera:

def registrar_usuario(servicio: ServicioNotificacion):
    notificador = Notificador(servicio)
    notificador.notificar("Bienvenido")

""" 
# En otra parte del código (MockService y SMSServices entre comillas para evitar alerta de error. Esto solo con fines demostrativos.):
registrar_usuario(EmailService())
registrar_usuario("MockService"())  # para pruebas unitarias
registrar_usuario("SMSService"())   # para un nuevo canal 

"""

Así logramos que registrar_usuario no cambie nunca, aunque cambie la tecnología detrás.

---
🎓 En resumen:

- DIP busca que el código de negocio no dependa de detalles técnicos.
- Ambos extremos (clases de lógica y clases técnicas) deben conectarse a través de una abstracción.
- En Python, esa abstracción se construye con clases abstractas y métodos obligatorios.
- Aplicar DIP mejora el desacoplamiento, permite reusar componentes, facilita las pruebas, y deja el sistema preparado para el cambio.

✅ Resultado: código limpio, mantenible y listo para escalar.
"""
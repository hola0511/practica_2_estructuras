import time
from control_mensajes import Mensajes

def iniciar_procesamiento(mensajes_obj: Mensajes):
    print("Procesando mensajes")
    mensajes_obj.clasificacion_de_mensajes()
    print("Mensajes clasificados y cargados en la cola de prioridad.")
    time.sleep(1)

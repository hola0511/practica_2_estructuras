import time
from control_mensajes import Mensajes

def iniciar_procesamiento(mensajes_obj: Mensajes):
    print("Procesando mensajes.")
    mensajes_obj.clasificacion_de_mensajes()
    print("Mensajes clasificados.")
    time.sleep(1)
    mensajes_obj.pug()
    numero, frecuencia = mensajes_obj.mayor_grupo()
    print(f"El numero mas repetido fue {numero} y se repite un total de {frecuencia}")


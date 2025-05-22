import time
from control_mensajes import Mensajes

def iniciar(mensajes_obj: Mensajes):
    print("Procesando mensajes.")
    mensajes_obj.clasificacion_de_mensajes()
    time.sleep(1)
    print("Mensajes clasificados.")
    time.sleep(1)
    mensajes_obj.pug()
    numero, frecuencia = mensajes_obj.mayor_grupo()
    time.sleep(1)
    print(f"El numero mas repetido fue {numero} y se repite un total de {frecuencia}")


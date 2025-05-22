import time
from agentes import Agente
from control_mensajes import Mensajes, EmptyQueue

def simular_atencion(agentes: list[Agente], mensajes_obj: Mensajes):
    while len(mensajes_obj.priority) > 0:
        for agente in sorted(agentes, key=lambda a: a.nivel_experiencia, reverse=True):
            if agente.estado == "disponible":
                try:
                    prioridad, mensaje = mensajes_obj.priority.dequeue()
                    agente.estado = "ocupado"
                    tiempo = agente.calcular_tiempo_respuesta(mensaje, prioridad)
                    print(f"\n [Agente {agente.id}] Atendiendo mensaje con prioridad {prioridad}...")
                    print(f"Mensaje: {mensaje}")
                    time.sleep(tiempo)
                    print(f" [Agente {agente.id}] Finalizó atención.")
                    agente.estado = "disponible"
                except EmptyQueue:
                    continue
        time.sleep(1)
    print("Todos los mensajes han sido atendidos.")

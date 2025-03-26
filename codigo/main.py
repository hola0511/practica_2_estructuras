from control_mensajes import Mensajes
from agentes import Agente
from procesador import iniciar_procesamiento
from simulador import simular_atencion

# Crear objeto de Mensajes (ya con la lista cargada en __init__)
mensajes = Mensajes(mensajes=[
    # Este contenido puede estar vacío si ya tienes tu mensajes.txt generado
])

# Crear agentes
agentes = [
    Agente(1, "experto"),
    Agente(2, "intermedio"),
    Agente(3, "basico"),
]

# Procesar mensajes y simular atención
iniciar_procesamiento(mensajes)
simular_atencion(agentes, mensajes)


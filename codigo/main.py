from control_mensajes import Mensajes
from agentes import Agente
from procesador import iniciar_procesamiento
from simulador import simular_atencion

# Crear objeto de Mensajes (ya con la lista cargada en __init__)
mensajes = Mensajes(mensajes = [
    "¿Cuál es el plan para reducir los retrasos en las entregas?",
    "El mantenimiento de la flota se está retrasando, ¿qué medidas se tomarán?",
    "¿Cómo podemos reducir el costo de combustible en las rutas más largas?",
    "El tráfico está afectando las entregas. ¿Hay soluciones disponibles?",
    "¿Se han producido accidentes en la ruta hoy?",
    "Estamos enfrentando un desabastecimiento de combustible, ¿cómo se solucionará?",
    "¿Hay suficientes conductores para cumplir con la demanda de entregas?",
    "¿Qué acciones se están tomando para mejorar la seguridad en las rutas?",
    "Los sistemas obsoletos están retrasando las entregas. ¿Qué planes hay para actualizarlos?",
    "¿Cómo está afectando la competencia en el mercado de transporte?",
    "¿Qué se está haciendo para reducir los costos de seguro de la flota?",
    "¿Cuál es el impacto de la sostenibilidad en las operaciones de la empresa?",
    "La logística está siendo un desafío en algunas rutas, ¿qué soluciones existen?",
    "Necesitamos optimizar la eficiencia operativa en las rutas de entrega.",
    "¿Qué cambios se han implementado en la gestión de flota para mejorar el rendimiento?",
    "¿Cómo se están abordando las faltas de cumplimiento normativo en el transporte?",
    "Los sistemas de comunicación no están funcionando correctamente, ¿cómo se puede mejorar?",
    "La ineficiencia en rutas está generando retrasos. ¿Qué alternativas existen?",
    "¿Qué medidas se están tomando para evitar sanciones por no cumplir con las normativas?",
    "El desgaste de vehículos está aumentando rápidamente, ¿qué se está haciendo al respecto?",
    "¿Cuáles son las principales causas de los retrasos en las entregas de hoy?",
    "El mantenimiento preventivo está siendo insuficiente, ¿cómo se pueden mejorar los tiempos?",
    "¿Qué medidas se están tomando para controlar el costo de combustible en la flota?",
    "¿Cuál es la estrategia para evitar el tráfico en rutas clave?",
    "¿Se han implementado medidas para reducir los accidentes en las entregas?",
    "¿Cómo se gestionará el desabastecimiento en las rutas más afectadas?",
    "¿Cómo podemos mejorar la seguridad en los vehículos y conductores?",
    "¿Cuáles son las acciones para actualizar los sistemas obsoletos de gestión?",
    "La competencia está afectando nuestra cuota de mercado, ¿cómo podemos mejorar?",
    "¿Qué iniciativas se están implementando para reducir los costos de seguro?",
    "¿Qué impacto tendrá la sostenibilidad en los procesos de distribución?",
    "¿Cómo se puede mejorar la logística para evitar retrasos en las entregas?",
    "¿Cuál es el plan para mejorar la eficiencia operativa en todas las rutas?",
    "¿Qué estrategias se están tomando para optimizar la gestión de flota?",
    "Las faltas de cumplimiento normativo están afectando nuestra operación. ¿Qué soluciones se proponen?",
    "La comunicación con los conductores es deficiente, ¿cómo se puede mejorar?",
    "¿Qué acciones se tomarán para reducir la ineficiencia en rutas?",
    "¿Cómo evitar las sanciones por no cumplir con las regulaciones de transporte?",
    "¿Qué se está haciendo para reducir el desgaste de vehículos en rutas largas?",
    "¿Cuáles son las soluciones para los retrasos causados por la congestión del tráfico?",
    "El mantenimiento de la flota requiere de más recursos, ¿qué se está haciendo al respecto?",
    "¿Cómo se están controlando los costos de combustible de forma eficiente?",
    "El tráfico está generando pérdidas económicas, ¿cómo podemos gestionarlo mejor?",
    "¿Qué medidas preventivas se están tomando para evitar accidentes en rutas peligrosas?",
    "¿Cuál es el plan para resolver el desabastecimiento de repuestos para los vehículos?",
    "¿Se están tomando medidas para optimizar la seguridad en zonas conflictivas?",
    "Necesitamos actualizar los sistemas obsoletos para mejorar la gestión de la flota.",
    "¿Qué estamos haciendo para mitigar el impacto de la competencia en el sector?",
    "¿Cómo podemos reducir los costos de seguro sin comprometer la cobertura?",
    "¿Qué estrategias se están implementando para garantizar la sostenibilidad de las operaciones?"
])

# Crear agentes
agentes = [
    Agente(1, "profesional"),
    Agente(2, "intermedio"),
    Agente(3, "basico"),
]

# Procesar mensajes y simular atención
iniciar_procesamiento(mensajes)
simular_atencion(agentes, mensajes)


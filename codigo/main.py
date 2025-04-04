from control_mensajes import Mensajes
from agentes import Agente
from procesador import iniciar_procesamiento
from simulador import simular_atencion

mensajes = Mensajes(mensajes = [
    "¿Cuál es el plan para reducir los retrasos en las entregas?",
    "El mantenimiento de la flota se está retrasando, ¿qué medidas se tomarán?",
    "¿Cómo podemos reducir el costo de combustible en las rutas más largas?",

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

agentes = [
    Agente(1, "profesional"),
    Agente(2, "intermedio"),
    Agente(3, "basico"),
    Agente(4, "profesional"),
    Agente(5, "basico"),
    Agente(6, "intermedio")
]

iniciar_procesamiento(mensajes)
simular_atencion(agentes, mensajes)


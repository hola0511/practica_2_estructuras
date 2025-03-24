class EmptyQueue(Exception):
    ...

class PriorityQueue:

    def __init__(self, priority: str):
        self.__queue: list[int] = []
        self.__priority: str = priority

    def enqueue(self, element: int):
        self.__queue.append(element)
        if self.__priority == "min":
            self.__queue.sort()
        elif self.__priority == "max":
            self.__queue.sort(reverse=True)

    def dequeue(self) -> int:
        if len(self.__queue) == 0:
            raise EmptyQueue("Cola Vacía...")
        return self.__queue.pop(0)

    def first(self) -> int:
        if len(self.__queue) == 0:
            raise EmptyQueue("Cola Vacía...")
        return self.__queue[0]

    def __repr__(self):
        return str(self.__queue)

    def __len__(self):
        return len(self.__queue)



class Mensajes:

    def __init__(self, mensajes: list):
        self.mensajes: list = mensajes
        self.palabras_clave: dict = {}
        self.priority: PriorityQueue = PriorityQueue("max")

    def clasificacion_de_mensajes(self, contador: int = 0):
        self.palabras_clave = {"Retrasos": 7, "Mantenimiento": 8, "Costo de combustible": 6, "Tráfico": 5,
                            "Accidentes": 10, "Desabastecimiento": 9, "Falta de conductores": 8, "Seguridad": 10,
                            "Loas ombsoletos": 6, "Competencia": 4, "Costos de seguro": 6, "Sostenibilidad": 5,
                            "Problegística": 7, "Eficiencia operativa": 6, "Gestión de flota": 7, "Faltas de cumplimiento normativo": 9,
                            "Sistemas de comunicación": 6, "Ineficiencia en rutas": 5, "Sanciones": 9, "Desgaste de vehículos": 7}

        with open("mensajes.txt", "w") as archivo:
            for mensaje in self.mensajes:
                archivo.write(mensaje + "\n")

        with open("mensajes.txt", "r") as archivo:
            lineas = archivo.readlines()
            print(lineas)
            for linea in lineas:
                contador = 0
                for clave, valor in self.palabras_clave.items():
                    if clave.lower() in linea.lower():
                        contador += valor
                self.priority.enqueue(contador)
        print(self.priority)
        return contador



mensajes = [
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
]


q = Mensajes(mensajes)
q.clasificacion_de_mensajes()

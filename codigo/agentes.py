class Agente:
    def __init__(self, id: int, nivel_experiencia: str):
        self.id: int = id
        self.nivel_experiencia: str = nivel_experiencia
        self.estado: str = "disponible"

    def calcular_tiempo_respuesta(self, mensaje: str, prioridad: float) -> float:
        longitud = len(mensaje.split())
        base = (longitud / 10) + (prioridad / 2)

        factor = {
            "basico": 1.0,
            "intermedio": 0.75,
            "profesional": 0.5
        }.get(self.nivel_experiencia.lower(), 1.0)

        return base * factor

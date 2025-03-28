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


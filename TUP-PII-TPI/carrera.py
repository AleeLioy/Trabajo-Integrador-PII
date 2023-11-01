
class Carrera:
    def __init__(self, nombre: str, cant_anios: int) -> None:
        self.__nombre = nombre
        self.__cant_anios = cant_anios
        self.__materias = []

    @property
    def nombre(self) -> str:
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre: str):
        self.__nombre = nuevo_nombre

    @property
    def cant_anios(self) -> int:
        return self.__cant_anios
    
    @cant_anios.setter
    def cant_anios(self, nueva_cant_anios: int):
        self.__cant_anios = nueva_cant_anios

    @property
    def materias(self) -> list:
        return self.__materias
    
    @materias.setter
    def materias(self, nueva_materia: list):
        self.__materias = nueva_materia

    def __str__(self) -> str:
        return f"Carrera: {self.nombre}"
    
    def get_cantidad_materias(self) -> int:
        return len(self.materias)
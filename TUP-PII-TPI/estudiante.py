from usuario import Usuario
from curso import Curso
from carrera import Carrera

class Estudiante(Usuario):
    def __init__(self, nombre: str, apellido: str, email: str, contrasenia: str, legajo: int, anio_inscripcion_carrera: int, carrera: Carrera) -> None:
        super().__init__(nombre, apellido, email, contrasenia)
        self.__legajo = legajo
        self.__anio_inscripcion_carrera = anio_inscripcion_carrera
        self.__mis_cursos = []
        self.__carrera = carrera

    @property
    def legajo(self):
        return self.__legajo
    
    @legajo.setter
    def legajo(self, nuevo_legajo):
        self.__legajo = nuevo_legajo

    @property
    def anio_inscripcion_carrera(self):
        return self.__anio_inscripcion_carrera
    
    @anio_inscripcion_carrera.setter
    def anio_inscripcion_carrera(self, nuevo_anio_inscripcion):
        self.__anio_inscripcion_carrera = nuevo_anio_inscripcion

    @property
    def mis_cursos(self) -> list:
        return self.__mis_cursos
    
    @property
    def carrera(self):
        return self.__carrera
    
    @carrera.setter
    def carrera(self, nueva_carrera):
        self.__carrera = nueva_carrera

    def __str__(self) -> str:
        return self.nombre

    def matricular_en_curso(self, curso) -> None:
        self.mis_cursos.append(curso)
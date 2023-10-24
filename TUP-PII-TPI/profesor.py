from usuario import Usuario

class Profesor(Usuario):
    def __init__(self, nombre: str, apellido: str, email: str, contrasenia: str, titulo: str, anio_egreso: int) -> None:
        super().__init__(nombre, apellido, email, contrasenia)
        self.__titulo = titulo
        self.__anio_egreso = anio_egreso
        self.__mis_cursos = []

    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def anio_egreso(self):
        return self.__anio_egreso
    
    @anio_egreso.setter
    def anio_egreso(self, anio_egreso):
        self.__anio_egreso = anio_egreso

    @property
    def mis_cursos(self):
        return self.__mis_cursos
    
    def __str__(self) -> str:
        return f"El profesor es: {self.nombre}"
    
    def dictar_curso(self, curso) -> None:
        self.mis_cursos.append(curso)
    
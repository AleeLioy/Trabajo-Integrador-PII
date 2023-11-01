from curso import Curso
from estudiante import Estudiante
from profesor import Profesor
from carrera import *

cursos = [
    Curso("Ingles I"),
    Curso("Ingles II"),
    Curso("Laboratorio I"),
    Curso("Laboratorio II"),
    Curso("Programacion I"),
    Curso("Programacion II")
]
nueva_carrera = Carrera("Tecnicatura Universitaria en Programación", 2)

carreras = [
    nueva_carrera
]

estudiantes = [
    Estudiante("Alejandro", "Lioy", "ale@gmail.com", "alelioy", 53047, 2023, nueva_carrera), 
    Estudiante("Matias", "Gioda", "mati@gmail.com", "matigioda", 53048, 2023, nueva_carrera)
]

profesores = [
    Profesor("Raul", "Rodriguez", "rodriguez@hotmail.com", "raulrodriguez", "Ingeniero en sistemas", 1998), 
    Profesor("Elena", "Estrella", "estrella@hotmail.com", "elenaestrella", "Ingeniero en sistemas", 1999) 
]


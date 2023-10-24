from curso import Curso
from estudiante import Estudiante
from profesor import Profesor

cursos = [
    Curso("Ingles I"),
    Curso("Ingles II"),
    Curso("Laboratorio I"),
    Curso("Laboratorio II"),
    Curso("Programacion I"),
    Curso("Programacion II")
]

estudiantes = [
    Estudiante("Alejandro", "Lioy", "ale@gmail.com", "alelioy", 53047, 2023), 
    Estudiante("Matias", "Gioda", "mati@gmail.com", "matigioda", 53048, 2023)
]

profesores = [
    Profesor("Raul", "Rodriguez", "rodriguez@hotmail.com", "raulrodriguez", "Ingeniero en sistemas", 1998), 
    Profesor("Elena", "Estrella", "estrella@hotmail.com", "elenaestrella", "Ingeniero en sistemas", 1999) 
]


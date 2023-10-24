import os
from datos import *
from usuario import *
from estudiante import *
from profesor import *

def menu_principal():
    print("1 - Ingresar como alumno.")
    print("2 - Ingresar como profesor.")
    print("3 - Ver cursos.")
    print("4 - Salir.")

def menu_alumno():
    print("1. Matricularse a un curso.")
    print("2. Ver curso.")
    print("3. Volver al menú principal")

def menu_profesor():
    print("1. Dictar curso.")
    print("2. Ver curso.")
    print("3. Volver al menú principal")

def credenciales(usuarios):
    email = input("Ingrese su email: ")
    clave = input("Ingrese su contraseña: ")
    for usuario in usuarios:
        if usuario.email == email:
            if usuario.validar_credenciales(email, clave):
                return "Usuario ingresado correctamente", True, usuario
            else:
                return "La contraseña ingresada es incorrecta", False, usuario
    return "Alumno no registrado", False, usuario

def ver_curso(usuario, curso):
    if isinstance(usuario, Estudiante):
        for curso_usuario in usuario.mis_cursos:
            if curso == curso_usuario:
                print(f"Nombre: {curso.nombre}")
                break
    else:
        for curso_usuario in usuario.mis_cursos:
            if curso == curso_usuario:
                print(f"Nombre: {curso.nombre}")
                print(f"Contraseña: {curso.contrasenia_matriculacion}")
                break

def ingreso_alumno(estudiante):
    cursos_disponibles = {}
    respuesta = ''
    while respuesta != "salir":
        menu_alumno()
        opciona = input("\n Ingrese una opcion: ")
        os.system ("cls")
        if opciona.isnumeric():
            if int(opciona) == 1:
                for i, curso in enumerate(cursos, 1):
                    cursos_disponibles[str(i)] = curso
                    print(f"{i} {curso.nombre}")
                opcionc = input("Ingrese el curso que quiere matricularse: ")
                curso_seleccionado = cursos_disponibles[str(i)]
                for curso_estudiante in estudiante.mis_cursos:
                    if curso_estudiante == curso_seleccionado:
                        print("Ya se encuentra matriculado en este curso.")
                        continue
                contrasenia_ingresada = input("Ingrese la contraseña de matriculación: ")
                if contrasenia_ingresada == curso_seleccionado.contrasenia_matriculacion:
                    print(f"Ya esta matriculado a la materia: {curso_seleccionado.nombre}")
                    estudiante.matricular_en_curso(curso_seleccionado)
                else:
                    print("Contraseña incorrecta.")
                    continue
            elif int(opciona) == 2:
                for i, curso in enumerate(estudiante.mis_cursos, 1):
                    cursos_disponibles[str(i)] = curso
                    print(f"{i} {curso.nombre}")
                opcionc = input("Ingrese el curso a visualizar: ")
                curso_seleccionado = cursos_disponibles[str(opcionc)]
                ver_curso(estudiante, curso_seleccionado)
            elif int(opciona) == 3:
                respuesta = "salir"
            else: 
                print("Ingrese una opción valida.")
        else: 
            print("Ingrese una opción valida.")

def ingreso_profesor(profesor):
    cursos_disponibles = {}
    respuesta = ''
    while respuesta != "salir":
        menu_profesor()
        opcionp = input("\n Ingrese una opcion: ")
        os.system ("cls")
        if opcionp.isnumeric():
            if int(opcionp) == 1:
                nombre_curso = input("Ingrese el nombre del curso a dictar: ")
                curso = Curso(nombre_curso)
                cursos.append(curso)
                profesor.dictar_curso(curso)
                print("Curso ingresado correctamente")
                ver_curso(profesor, curso)
            elif int(opcionp) == 2:
                for i, curso in enumerate(profesor.mis_cursos, 1):
                    cursos_disponibles[str(i)] = curso
                    print(f"{i} {curso.nombre}")
                opcionc = input("Ingrese el curso a visualizar: ")
                curso_seleccionado = cursos_disponibles[str(opcionc)]
                ver_curso(profesor, curso_seleccionado)
            elif int(opcionp) == 3:
                respuesta = "salir"
            else: 
                print("Ingrese una opcion valida.")
        else: 
            print("Ingrese una opcion numerica.")


print("Bienvenido/a al campus virtual!")
respuesta = ''

while respuesta != "salir":
    menu_principal()
    opcion = input("\n Ingrese una opcion: ")
    os.system ("cls")
    if opcion.isnumeric():
        if int(opcion) == 1:
            mensaje, validacion, estudiante = credenciales(estudiantes)
            if validacion:
                print(mensaje)
            else:
                print(mensaje)
                continue
            ingreso_alumno(estudiante)
        elif int(opcion) == 2:
            mensaje, validacion, profesor = credenciales(profesores)
            if validacion:
                print(mensaje)
            else:
                print(mensaje)
                continue
            ingreso_profesor(profesor)
        elif int(opcion) == 3:
            for curso in cursos:
                print(f"{curso} Carrera: Tecnicatura Universitaria en Programación")
        elif int(opcion) == 4:
            respuesta = "salir"
        else: print("Ingrese una opcion valida.")
    else: 
        print("Ingrese una opcion numerica.")
    
    input("Precione cualquier tecla para volver al menu")

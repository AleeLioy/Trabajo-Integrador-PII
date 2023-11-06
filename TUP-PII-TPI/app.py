import os
from datos import *
from usuario import *
from estudiante import*
from profesor import *
from carrera import *
from archivo import *
from typing import Union

def menu_principal():
    print("1 - Ingresar como alumno.")
    print("2 - Ingresar como profesor.")
    print("3 - Ver cursos.")
    print("4 - Salir.")

def menu_alumno():
    print("1. Matricularse a un curso.")
    print("2. Desmatricularse de un curso.")
    print("3. Ver cursos.")
    print("4. Volver al menú principal")

def menu_profesor():
    print("1. Dictar curso.")
    print("2. Ver curso.")
    print("3. Volver al menú principal")

def credenciales(usuarios: list) -> Union[bool, Usuario]:
    email = input("Ingrese su email: ")
    for usuario in usuarios:
        if usuario.email == email:
            clave = input("Ingrese su contraseña: ")
            if usuario.validar_credenciales(email, clave):
                print ("Usuario ingresado correctamente")
                return True, usuario
            else:
                print("La contraseña ingresada es incorrecta")
                return False, usuario
    print("El email ingresado no se encuentra registrado")

    es_profesor = input("Si es profesor ingrese el codigo admin, de lo contrario presione enter: ")
    
    if es_profesor.lower() == "admin":
        registrar_profesor()
    return False, usuario

def ver_archivos(curso: Curso):
    if len(curso.archivos) != 0:
        print("Archivos de la materia: ")
        for archivo in sorted(curso.archivos, key=lambda archivo: archivo.fecha):
            print(archivo)

def registrar_profesor():

    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    email = input("Ingrese su email: ")

    for profesor in profesores:
        if profesor.email == email:
            print("El email se encuentra registrado. Presione enter para volver al menu principal.")
            return
        
    clave = input("Ingrese una contraseña: ")
    titulo = input("Ingrese su título: ")
    anio_egreso = input("ingrese el año de egreso: ")

    profesores.append(Profesor(nombre, apellido, email, clave, titulo, anio_egreso))

    print("Registrado correctamente.")

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

def listar_cursos(lista: list, mensaje: str) -> Curso:

    lista_disponibles = {}
    if len(lista) != 0:
        for i, item in enumerate(lista, 1):
            lista_disponibles[str(i)] = item
            print(f"{i} {item.nombre}")
        while True:
            opt_item = input(mensaje)
            if not opt_item.isnumeric() or int(opt_item) < 1 or int(opt_item) > len(lista):
                print("La opcion ingresada es invalida")
                continue
            break
        return lista_disponibles[str(opt_item)]
    else:
        return None


def mostrar_cursos(usuario: object, identificador: int):

    curso_seleccionado = listar_cursos(usuario.mis_cursos, "Ingrese la opcion correspondiente para ver más informacion: ")

    if curso_seleccionado is not None:
        ver_curso(usuario, curso_seleccionado, identificador)
        if isinstance(usuario, Profesor):
            desea_cargar = input("Desea cargar un archivo? S/N: ")
            if desea_cargar.upper() == "S":
                agregar_archivo(curso_seleccionado)
    else:
        print("No hay cursos cargados.")


def esta_matriculado(estudiante: Estudiante, curso: Curso) -> bool:

    for curso_estudiante in estudiante.mis_cursos:
        if curso_estudiante == curso:
            print("Usted ya se encuentra matriculado en este curso.")
            return True
    return False


def matricularse_curso(estudiante: Estudiante):

    curso_seleccionado = listar_cursos(estudiante.carrera.materias, "Ingrese el curso que quiere matricularse: ")

    if curso_seleccionado is not None:
        if esta_matriculado(estudiante, curso_seleccionado):
            return
        contrasenia_ingresada = input("Ingrese la contraseña de matriculación: ")
        if contrasenia_ingresada == curso_seleccionado.contrasenia_matriculacion:
            estudiante.matricular_en_curso(curso_seleccionado)
            print(f"Usted se ha matriculado exitosamente!!: {curso_seleccionado.nombre}")
        else:
            print("La contraseña de matriculación ingresada es incorrecta.")
    else:
        print("No hay cursos cargados.")


def desmatricular_curso(estudiante: Estudiante):

    curso_seleccionado = listar_cursos(estudiante.mis_cursos, "Ingrese el curso del cual desea desmatricularse: ")

    if curso_seleccionado is not None:
        estudiante.desmatricular_curso(curso_seleccionado)
        print("Usted se desmatriculo exitosamente.")
    else:
        print("Usted no posee matriculaciones activas.")


def agregar_archivo(curso: Curso):
    while True:
        nombre = input("Ingrese el nombre del archivo: ")
        formato = input("Ingrese el formato del archivo: ")
        nuevo_archivo = Archivo(nombre, formato)
        curso.nuevo_archivo(nuevo_archivo)

        print(f"Se agrego el archivo: {nuevo_archivo}")
        opt_archivo = input("Desea agregar otro archivo?(S/N)")
        if opt_archivo.upper() != "S":
            return


def dictar_nuevo_curso(profesor: Profesor, identificador: int):
    nombre_curso = input("Ingrese el nombre del curso a dictar: ")
    curso = Curso(nombre_curso)
    carrera_seleccionada = listar_cursos(carreras, "Ingrese la carrera: ")
    carrera_seleccionada.materias.append(curso)
    profesor.dictar_curso(curso)

    print("El curso ha sido ingresado correctamente.")

    ver_curso(profesor, curso, identificador)


def ver_cursos_alfabeticamente():

    carreras_ordenadas = sorted(carreras, key=lambda carrera: carrera.nombre)
    for carrera in carreras_ordenadas:
        materias_ordenadas = sorted(carrera.materias, key=lambda materia: materia.nombre)

        for materia in materias_ordenadas:
            print(f"{materia} - {carrera}")

def ingreso_alumno(estudiante: Estudiante):

    respuesta = ''
    indentificador_alumno = 1
    while respuesta != "salir":
        menu_alumno()
        opt_alumno = input("\n Ingrese la opción de menu: ")
        os.system("cls")
        if opt_alumno.isnumeric():
            if int(opt_alumno) == 1:
                matricularse_curso(estudiante)
            elif int(opt_alumno) == 2:
                desmatricular_curso(estudiante)
            elif int(opt_alumno) == 3:
                mostrar_cursos(estudiante, indentificador_alumno)
            elif int(opt_alumno) == 4:
                respuesta = "salir"
            else:
                print("Ingrese una opcion valida.")
        else:
            print("Ingrese una opcion numerica.")

def ingreso_profesor(profesor: Profesor):
    
    respuesta = ''
    indentificador_profesor = 2
    while respuesta != "salir":
        menu_profesor()
        opt_profesor = input("\nIngrese la opción de menu: ")
        os.system("cls")
        if opt_profesor.isnumeric():
            if int(opt_profesor) == 1:
                dictar_nuevo_curso(profesor, indentificador_profesor)
            elif int(opt_profesor) == 2:
                mostrar_cursos(profesor, indentificador_profesor)
            elif int(opt_profesor) == 3:
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
            validacion, estudiante = credenciales(estudiantes)
            if validacion:
                ingreso_alumno(estudiante)
        elif int(opcion) == 2:
            validacion, profesor = credenciales(profesores)
            if validacion:
                ingreso_profesor(profesor)
        elif int(opcion) == 3:
            ver_cursos_alfabeticamente()
        elif int(opcion) == 4:
            respuesta = "salir"
        else: print("Ingrese una opcion valida.")
    else: 
        print("Ingrese una opcion numerica.")
    
    input("Precione cualquier tecla para volver al menu")

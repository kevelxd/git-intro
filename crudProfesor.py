#CRUD de profesor
#NOMBRE: KEVIN ESCOBAR MARTINEZ
#NUM CONTROL: 22270522
#PRACTICA: 12

import mysql.connector

def conectar():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='alee',
        database='dbtaller'
    )


def mostrarProfesor():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM profesor;')
    print('Lista de profesores 👇📝:')
    for clave, nombre in cursor.fetchall():
        print(f'Clave: {clave}, Nombre: {nombre}')
    print('\n')


def agregarProfesor():
    clave = input('Ingresa la clave para el nuevo profesor: ')
    nombre = input('Ingresa el nombre para el nuevo profesor: ')
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('INSERT INTO profesor (clave_profesor, nombre_profesor) VALUES (%s, %s)', (clave, nombre))
    conexion.commit()
    print('Profesor agregado 🙀\n')


def actualizarProfesor():
    clave = input('Ingresa la clave del profesor para actualizar: ')
    nuevo_nombre = input('Ingresa el nuevo nombre: ')
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('UPDATE profesor SET nombre_profesor = %s WHERE clave_profesor = %s', (nuevo_nombre, clave))
    conexion.commit()
    print('Profesor actualizado 🔁\n')


def eliminarProfesor():
    clave = input('Ingresa la clave del profesor a eliminar: ')
    conexion = conectar()
    cursor =  conexion.cursor()
    cursor.execute('DELETE FROM profesor WHERE clave_profesor = %s', (clave,))
    conexion.commit()
    print('Profesor eliminado ⚠️\n')


def menu():
    while True:
        print('Elije una opcion.')
        print('\ta) Mostrar tipos de proyectos')
        print('\tb) Agregar tipo de proyecto.')
        print('\tc) Actualizar tipo de proyecto.')
        print('\td) Eliminar tito de proyecto.')
        print('\te) Salir')
        opcion = input('Seleccion: ')
        opcion = opcion.lower()

        if opcion == 'e' or  opcion == 'exit':
            break

        elif opcion == 'a':
            mostrarProfesor()

        elif opcion == 'b':
            agregarProfesor()

        elif opcion == 'c':
            actualizarProfesor()

        elif opcion == 'd':
            eliminarProfesor()

        else:
            print('Elije una opcion valida\n')

        
if __name__ == '__main__':
    menu()
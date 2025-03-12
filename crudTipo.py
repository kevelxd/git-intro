#CRUD de tipo
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


def mostrarTipos():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM tipoproyec;')
    print('Lista de tipos 👇📝:')
    for clave, nombre in cursor.fetchall():
        print(f'Clave: {clave}, Nombre: {nombre}')
    print('\n')


def agregarTipo():
    clave = input('Ingresa la clave para el tipo de proyecto: ')
    nombre = input('Ingresa el nombre para el tipo de proyecto: ')
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('INSERT INTO tipoproyec (clave_tipo, nombre_tipo) VALUES (%s, %s)', (clave, nombre))
    conexion.commit()
    print('Tipo agregado 📝\n')


def actualizarTipo():
    clave = input('Ingresa la clave del tipo para actualizar: ')
    nuevo_nombre = input('Ingresa el nuevo nombre: ')
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('UPDATE tipoproyec SET nombre_tipo = %s WHERE clave_tipo = %s', (nuevo_nombre, clave))
    conexion.commit()
    print('Tipo actualizado 🔁\n')


def eliminarTipo():
    clave = input('Ingresa la clave del tipo a eliminar: ')
    conexion = conectar()
    cursor =  conexion.cursor()
    cursor.execute('DELETE FROM tipoproyec WHERE clave_tipo = %s', (clave,))
    conexion.commit()
    print('Tipo eliminado ⚠️\n')


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
            print('🫡')
            break

        elif opcion == 'a':
            mostrarTipos()

        elif opcion == 'b':
            agregarTipo()

        elif opcion == 'c':
            actualizarTipo()

        elif opcion == 'd':
            eliminarTipo()

        else:
            print('Elije una opcion valida\n')

        
if __name__ == '__main__':
    menu()
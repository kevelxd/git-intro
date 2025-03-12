import mysql.connector

def conexion_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="alee",
        database="dbtaller"
    )

def agregar_categoria():
    descripcion = input("Ingrese la descripción de la categoría: ")
    conexion = conexion_db()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO tipoproyecto (nombre_tipo) VALUES (%s)", (descripcion,))
    conexion.commit()
    conexion.close()
    print("Categoría añadida con éxito.")


def listar_categorias():
    conexion = conexion_db()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM tipoproyecto")
    for id_categoria, descripcion in cursor.fetchall():
        print(f"Código: {id_categoria}, Descripción: {descripcion}")
    conexion.close()


def modificar_categoria():
    id_categoria = int(input("Ingrese el código de la categoría a modificar: "))
    nueva_descripcion = input("Ingrese la nueva descripción: ")
    conexion = conexion_db()
    cursor = conexion.cursor()
    cursor.execute("UPDATE tipoproyecto SET nombre_tipo = %s WHERE clave_tipo = %s", (nueva_descripcion, id_categoria))
    conexion.commit()
    conexion.close()
    print("Categoría actualizada correctamente.")


def borrar_categoria():
    id_categoria = int(input("Ingrese el código de la categoría a eliminar: "))
    conexion = conexion_db()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM tipoproyecto WHERE clave_tipo = %s", (id_categoria,))
    conexion.commit()
    conexion.close()
    print("Categoría eliminada exitosamente.")


def menu():
    while True:
        print("\n1. Añadir categoría")
        print("2. Ver categorías")
        print("3. Editar categoría")
        print("4. Eliminar categoría")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_categoria()
        elif opcion == "2":
            listar_categorias()
        elif opcion == "3":
            modificar_categoria()
        elif opcion == "4":
            borrar_categoria()
        elif opcion == "5":
            print("Cerrando el programa...")
            break
        else:
            print("Selección inválida, intente nuevamente.")


if __name__ == "__main__":
    menu()

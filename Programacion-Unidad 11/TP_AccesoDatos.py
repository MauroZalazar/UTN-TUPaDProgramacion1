import sqlite3

NOMBRE_DB = "biblioteca.db"

# Función única de conexión centralizada
def conectar():
    return sqlite3.connect(NOMBRE_DB)

# ----------------- CLASES (Modelo POO) -----------------

class Autor:
    def __init__(self, id_autor, nombre, nacionalidad):
        self.id_autor = id_autor
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def __str__(self):
        return f"ID: {self.id_autor} | Nombre: {self.nombre} | Nacionalidad: {self.nacionalidad}"
    
class Libro:
    def __init__(self, id_libro, titulo, anio_publicacion, autor):
        self.id_libro = id_libro
        self.titulo = titulo
        self.anio_publicacion = anio_publicacion
        self.autor = autor

    def __str__(self):
        return f"ID: {self.id_libro} | Título: {self.titulo} | Año: {self.anio_publicacion} | Autor: {self.autor.nombre}"


# ----------------- INICIALIZACIÓN DE LA BASE DE DATOS -----------------

def inicializar_base_datos():
    conexion = conectar()
    cursor = conexion.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS autores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            nacionalidad TEXT NOT NULL)''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS libros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            anio INTEGER NOT NULL,
            autor_id INTEGER NOT NULL,
            FOREIGN KEY (autor_id) REFERENCES autores(id))''')

    conexion.commit()
    conexion.close()


# ----------------- OPERACIONES CRUD (REPOSITORIO) -----------------

def registrar_autor(nombre, nacionalidad):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO autores (nombre, nacionalidad) VALUES (?, ?)", (nombre, nacionalidad))
    conexion.commit()
    id_generado = cursor.lastrowid
    conexion.close()
    return id_generado

def listar_autores():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT id, nombre, nacionalidad FROM autores")
    filas = cursor.fetchall()
    conexion.close()
    
    if not filas:
        print("\nNo hay autores registrados.")
        return False
    
    print("\n--- LISTA DE AUTORES ---")
    for fila in filas:
        print(f"ID: {fila[0]} | Nombre: {fila[1]} | Nacionalidad: {fila[2]}")
    return True

def eliminar_autor(id_autor):
    conexion = conectar()
    cursor = conexion.cursor()
    
    # Opcional pero recomendado: Primero eliminamos los libros asociados a este autor 
    # para evitar errores de restricción de Clave Foránea (Foreign Key)
    cursor.execute("DELETE FROM libros WHERE autor_id = ?", (id_autor,))
    
    # Luego eliminamos el autor
    cursor.execute("DELETE FROM autores WHERE id = ?", (id_autor,))
    filas_afectadas = cursor.rowcount
    
    conexion.commit()
    conexion.close()
    return filas_afectadas > 0

def registrar_libro(titulo, anio, autor_id):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO libros (titulo, anio, autor_id) VALUES (?, ?, ?)", (titulo, anio, autor_id))
    conexion.commit()
    id_generado = cursor.lastrowid
    conexion.close()
    return id_generado
    
def listar_libros():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('''
        SELECT libros.id, libros.titulo, libros.anio, autores.nombre
        FROM libros
        JOIN autores ON libros.autor_id = autores.id''')
    filas = cursor.fetchall()
    conexion.close()
    
    if not filas:
        print("\nNo hay libros registrados.")
        return False

    print("\n--- LISTA DE LIBROS ---")
    for fila in filas:
        print(f"ID: {fila[0]} | Título: {fila[1]} | Año: {fila[2]} | Autor: {fila[3]}")
    return True

def actualizar_titulo_libro(id_libro, nuevo_titulo):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("UPDATE libros SET titulo = ? WHERE id = ?", (nuevo_titulo, id_libro))
    filas_afectadas = cursor.rowcount
    conexion.commit()
    conexion.close()
    return filas_afectadas > 0

def eliminar_libro(id_libro):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM libros WHERE id = ?", (id_libro,))
    filas_afectadas = cursor.rowcount
    conexion.commit()
    conexion.close()
    return filas_afectadas > 0


# ----------------- MENÚ INTERACTIVO (DINÁMICO) -----------------

def menu():
    inicializar_base_datos()
    
    while True:
        print("\n==============================")
        print("    SISTEMA DE BIBLIOTECA     ")
        print("==============================")
        print("1. Registrar Autor")
        print("2. Listar Autores")
        print("3. Eliminar Autor")  # <--- Opción nueva agregada
        print("4. Registrar Libro")
        print("5. Listar Libros")
        print("6. Actualizar Título de Libro")
        print("7. Eliminar Libro")
        print("8. Salir")
        
        opcion = input("\nSeleccione una opción (1-8): ").strip()
        
        if opcion == "1":
            nombre = input("Ingrese el nombre del autor: ").strip()
            nacionalidad = input("Ingrese la nacionalidad: ").strip()
            if nombre and nacionalidad:
                id_generado = registrar_autor(nombre, nacionalidad)
                print(f"¡Autor registrado con éxito! ID asignado: {id_generado}")
            else:
                print("Error: Los campos no pueden estar vacíos.")
                
        elif opcion == "2":
            listar_autores()
            input("\nPresione Enter para continuar...")
            
        elif opcion == "3":  # <--- Lógica para la nueva opción de eliminar autor
            hay_autores = listar_autores()
            if hay_autores:
                try:
                    id_autor = int(input("Ingrese el ID del autor que desea eliminar: "))
                    if eliminar_autor(id_autor):
                        print("¡Autor (y sus libros asociados) eliminados correctamente!")
                    else:
                        print("No se encontró un autor con ese ID.")
                except ValueError:
                    print("Error: Ingrese un ID numérico válido.")
            
        elif opcion == "4":
            hay_autores = listar_autores()
            if hay_autores:
                try:
                    autor_id = int(input("Ingrese el ID del autor para el libro: "))
                    titulo = input("Ingrese el título del libro: ").strip()
                    anio = int(input("Ingrese el año de publicación: "))
                    if titulo:
                        id_generado = registrar_libro(titulo, anio, autor_id)
                        print(f"¡Libro registrado con éxito! ID asignado: {id_generado}")
                    else:
                        print("Error: El título no puede estar vacío.")
                except ValueError:
                    print("Error: Ingrese valores numéricos válidos para el ID y el año.")
            
        elif opcion == "5":
            listar_libros()
            input("\nPresione Enter para continuar...")
            
        elif opcion == "6":
            hay_libros = listar_libros()
            if hay_libros:
                try:
                    id_libro = int(input("Ingrese el ID del libro que desea actualizar: "))
                    nuevo_titulo = input("Ingrese el nuevo título: ").strip()
                    if nuevo_titulo and actualizar_titulo_libro(id_libro, nuevo_titulo):
                        print("¡Título actualizado correctamente!")
                    else:
                        print("No se encontró un libro con ese ID o el título está vacío.")
                except ValueError:
                    print("Error: Ingrese un ID válido.")
                    
        elif opcion == "7":
            hay_libros = listar_libros()
            if hay_libros:
                try:
                    id_libro = int(input("Ingrese el ID del libro que desea eliminar: "))
                    if eliminar_libro(id_libro):
                        print("¡Libro eliminado correctamente!")
                    else:
                        print("No se encontró un libro con ese ID.")
                except ValueError:
                    print("Error: Ingrese un ID válido.")
                    
        elif opcion == "8":
            print("\n¡Saliendo del sistema de biblioteca! ¡Mucho éxito con el estudio!")
            break
        else:
            print("Opción inválida. Por favor, elija un número del 1 al 8.")

if __name__ == "__main__":
    menu()
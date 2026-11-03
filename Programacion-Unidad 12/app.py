from flask import Flask, jsonify, request
import sqlite3
import os

app = Flask(__name__)

# Esto detecta automáticamente la carpeta donde está tu app.py y busca biblioteca.db ahí al lado
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
NOMBRE_DB = os.path.join(BASE_DIR, "biblioteca.db")

def conectar():
    return sqlite3.connect(NOMBRE_DB)

# ----------------- ENDPOINTS DE AUTORES -----------------

@app.route('/api/autores', methods=['GET'])
def obtener_autores():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT id, nombre, nacionalidad FROM autores")
    filas = cursor.fetchall()
    conexion.close()

    autores = []
    for fila in filas:
        autores.append({
            "id": fila[0],
            "nombre": fila[1],
            "nacionalidad": fila[2]
        })
    return jsonify(autores), 200

@app.route('/api/autores', methods=['POST'])
def crear_autor():
    datos = request.get_json()
    if not datos or 'nombre' not in datos or 'nacionalidad' not in datos:
        return jsonify({'error': 'Datos incompletos. Se requiere nombre y nacionalidad.'}), 400

    nombre = datos['nombre']
    nacionalidad = datos['nacionalidad']

    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO autores (nombre, nacionalidad) VALUES (?, ?)", (nombre, nacionalidad))
    conexion.commit()
    id_generado = cursor.lastrowid
    conexion.close()

    nuevo_autor = {
        "id": id_generado,
        "nombre": nombre,
        "nacionalidad": nacionalidad
    }
    return jsonify(nuevo_autor), 201


# ----------------- ENDPOINTS DE LIBROS -----------------

@app.route('/api/libros', methods=['GET'])
def obtener_libros():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('''
        SELECT libros.id, libros.titulo, libros.anio, autores.id, autores.nombre, autores.nacionalidad
        FROM libros
        JOIN autores ON libros.autor_id = autores.id
    ''')
    filas = cursor.fetchall()
    conexion.close()

    libros = []
    for fila in filas:
        libros.append({
            "id": fila[0],
            "titulo": fila[1],
            "anio": fila[2],
            "autor": {
                "id": fila[3],
                "nombre": fila[4],
                "nacionalidad": fila[5]
            }
        })
    return jsonify(libros), 200

@app.route('/api/libros/<int:id_libro>', methods=['GET'])
def obtener_libro_por_id(id_libro):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('''
        SELECT libros.id, libros.titulo, libros.anio, autores.id, autores.nombre, autores.nacionalidad
        FROM libros
        JOIN autores ON libros.autor_id = autores.id
        WHERE libros.id = ?
    ''', (id_libro,))
    fila = cursor.fetchone()
    conexion.close()

    if not fila:
        return jsonify({'error': 'Libro no encontrado'}), 404

    libro = {
        "id": fila[0],
        "titulo": fila[1],
        "anio": fila[2],
        "autor": {
            "id": fila[3],
            "nombre": fila[4],
            "nacionalidad": fila[5]
        }
    }
    return jsonify(libro), 200

@app.route('/api/libros', methods=['POST'])
def crear_libro():
    datos = request.get_json()
    if not datos or 'titulo' not in datos or 'anio' not in datos or 'autor_id' not in datos:
        return jsonify({'error': 'Datos incompletos. Se requiere titulo, anio y autor_id.'}), 400

    titulo = datos['titulo']
    anio = datos['anio']
    autor_id = datos['autor_id']

    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT id FROM autores WHERE id = ?", (autor_id,))
    if not cursor.fetchone():
        conexion.close()
        return jsonify({'error': 'El autor especificado no existe'}), 404

    cursor.execute("INSERT INTO libros (titulo, anio, autor_id) VALUES (?, ?, ?)", (titulo, anio, autor_id))
    conexion.commit()
    id_generado = cursor.lastrowid
    conexion.close()

    nuevo_libro = {
        "id": id_generado,
        "titulo": titulo,
        "anio": anio,
        "autor_id": autor_id
    }
    return jsonify(nuevo_libro), 201

@app.route('/api/libros/<int:id_libro>', methods=['PUT'])
def actualizar_libro(id_libro):
    datos = request.get_json()
    if not datos:
        return jsonify({'error': 'No se enviaron datos para actualizar'}), 400

    conexion = conectar()
    cursor = conexion.cursor()
    
    cursor.execute("SELECT id, titulo, anio, autor_id FROM libros WHERE id = ?", (id_libro,))
    libro_actual = cursor.fetchone()
    if not libro_actual:
        conexion.close()
        return jsonify({'error': 'Libro no encontrado'}), 404

    nuevo_titulo = datos.get('titulo', libro_actual[1])
    nuevo_anio = datos.get('anio', libro_actual[2])
    nuevo_autor_id = datos.get('autor_id', libro_actual[3])

    cursor.execute("UPDATE libros SET titulo = ?, anio = ?, autor_id = ? WHERE id = ?", 
                   (nuevo_titulo, nuevo_anio, nuevo_autor_id, id_libro))
    conexion.commit()
    conexion.close()

    return jsonify({
        'mensaje': 'Libro actualizado correctamente',
        'id': id_libro,
        'titulo': nuevo_titulo,
        'anio': nuevo_anio,
        'autor_id': nuevo_autor_id
    }), 200

@app.route('/api/libros/<int:id_libro>', methods=['DELETE'])
def eliminar_libro(id_libro):
    conexion = conectar()
    cursor = conexion.cursor()
    
    cursor.execute("SELECT id FROM libros WHERE id = ?", (id_libro,))
    if not cursor.fetchone():
        conexion.close()
        return jsonify({'error': 'Libro no encontrado'}), 404

    cursor.execute("DELETE FROM libros WHERE id = ?", (id_libro,))
    conexion.commit()
    conexion.close()

    return jsonify({'mensaje': 'Libro eliminado correctamente', 'id': id_libro}), 200


if __name__ == '__main__':
    app.run(debug=True, port=5000)

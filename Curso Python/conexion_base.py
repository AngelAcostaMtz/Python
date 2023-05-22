"""Modulo para el CRUD de Prueba con Flask"""
import uuid
from flask import Flask, jsonify, request
import psycopg2
from flask_cors import CORS
from psycopg2.extras import UUID_adapter
psycopg2.extensions.register_adapter(uuid.UUID, UUID_adapter)
#Conexion a la base de datos en Postgres

conn = psycopg2.connect(
    dbname = "biblioteca",
    user ="postgres",
    password = "angel",
    host = "localhost",
    port = "5432"
)

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

#Obtener todos los libros
@app.route('/api/libros', methods=['GET'])
def obtener_todos():
    """obteniendo los libros"""
    cur = conn.cursor()
    cur.execute("select * from libros where activo = true")
    rows = cur.fetchall()
    libros = []
    for row in rows:
        libro = {"Id": row[0], "Titulo": row[1], "Autor": row[2]}
        libros.append(libro)
    return jsonify(libros)

#acceder a un libro por su ID
@app.route('/api/libros/<int:libros_id>', methods=['GET'])
def get_libro(libros_id):
    """obteniendo los libros por id"""
    cur = conn.cursor()
    cur.execute("SELECT * FROM libros WHERE Id = %s", (libros_id,))
    row = cur.fetchone()
    if row is None:
        return jsonify({"error":"libro no existe"})
    libro = {"Id": row[0], "Titulo": row[1], "Autor": row[2]}
    return jsonify(libro)

#agregar un libro a la base de datos
@app.route('/api/libros', methods=['POST'])
def crear_libro():
    """Agregando Libro a la base de datos"""
    libro = request.json
    titulo = libro.get('Titulo')
    autor = libro.get('Autor')
    cur = conn.cursor()
    cur.execute("INSERT INTO libros (titulo, autor, activo) VALUES (%s, %s, true)", (titulo, autor))
    conn.commit()
    cur.execute("SELECT id FROM libros WHERE titulo = %s AND autor = %s", (titulo, autor))
    libro_id = cur.fetchone()[0]
    return jsonify({"Id": libro_id, "Titulo": titulo, "Autor": autor})

@app.route('/api/libros/<int:id>', methods=['PUT'])
def actualizar_libro(id):
    """Actualizar Libro por id"""
    libro = request.json
    titulo = libro.get('titulo')
    autor = libro.get('autor')
    cur = conn.cursor()
    cur.execute("UPDATE libros SET titulo = %s, autor = %s WHERE id = %s", (titulo, autor, id))
    conn.commit()
    cur.execute("SELECT id FROM libros WHERE titulo = %s AND autor = %s", (titulo, autor))
    libro_id = cur.fetchone()[0]
    return jsonify({"id": libro_id, "titulo": titulo, "autor": autor})

@app.route('/api/libros/<int:id>', methods=['DELETE'])
def eliminar_libro(id):
    """Eliminar Libro por id"""
    cur = conn.cursor()
    cur.execute("update libros set activo = false WHERE id = %s", (id,))
    conn.commit()
    return jsonify({"mensaje": "Libro eliminado correctamente"})

if __name__ == '__main__':
    app.run(debug=True)
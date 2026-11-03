import requests

# URL base donde corre tu API Flask
BASE_URL = "http://127.0.0.1:5000/api"

def probar_api():
    print("=== INICIANDO PRUEBAS AUTOMÁTICAS DE LA API ===")
    
    # 1. Probar GET /api/libros (Listar libros iniciales)
    print("\n1. Probando GET /api/libros...")
    response = requests.get(f"{BASE_URL}/libros")
    print(f"Código de estado (Esperado 200): {response.status_code}")
    print("Respuesta:", response.json())
    
    # 2. Probar POST /api/autores (Crear un autor nuevo)
    print("\n2. Probando POST /api/autores...")
    autor_data = {"nombre": "Jorge Luis Borges", "nacionalidad": "Argentina"}
    response = requests.post(f"{BASE_URL}/autores", json=autor_data)
    print(f"Código de estado (Esperado 201): {response.status_code}")
    autor_creado = response.json()
    print("Autor creado:", autor_creado)
    autor_id = autor_creado["id"]

    # 3. Probar POST /api/libros (Crear un libro asociado al autor recién creado)
    print("\n3. Probando POST /api/libros...")
    libro_data = {"titulo": "Ficciones", "anio": 1944, "autor_id": autor_id}
    response = requests.post(f"{BASE_URL}/libros", json=libro_data)
    print(f"Código de estado (Esperado 201): {response.status_code}")
    libro_creado = response.json()
    print("Libro creado:", libro_creado)
    libro_id = libro_creado["id"]

    # 4. Probar PUT /api/libros/<id> (Actualizar el título del libro)
    print(f"\n4. Probando PUT /api/libros/{libro_id}...")
    update_data = {"titulo": "Ficciones (Edición Revisada)"}
    response = requests.put(f"{BASE_URL}/libros/{libro_id}", json=update_data)
    print(f"Código de estado (Esperado 200): {response.status_code}")
    print("Respuesta:", response.json())

    # 5. Probar DELETE /api/libros/<id> (Eliminar el libro creado)
    print(f"\n5. Probando DELETE /api/libros/{libro_id}...")
    response = requests.delete(f"{BASE_URL}/libros/{libro_id}")
    print(f"Código de estado (Esperado 200): {response.status_code}")
    print("Respuesta:", response.json())
    
    print("\n=== ¡TODAS LAS PRUEBAS FINALIZARON CON ÉXITO! ===")

if __name__ == "__main__":
    probar_api()
#Punto 1

precios_frutas = {"Banana": 1200, "Ananá": 2500, "Melón": 3000, "Uva": 1450}

precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

print("Ejercicio 1:", precios_frutas)
print("\n" + "=" * 40 + "\n")

#Punto 2

precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

print("Ejercicio 2 (Actualizado):", precios_frutas)
print("\n" + "=" * 40 + "\n")

#Punto 3

lista_frutas = list(precios_frutas.keys())

print("Ejercicio 3 (Solo frutas):", lista_frutas)
print("\n" + "=" * 40 + "\n")

#Punto 4

contactos = {}

print("--- Carga de 5 Contactos ---")
for i in range(5):
    nombre = input(f"Ingresá el nombre del contacto {i+1}: ")
    telefono = input(f"Ingresá el teléfono de {nombre}: ")
    contactos[nombre] = telefono

print()
consulta = input("¿Qué contacto querés buscar?: ")

if consulta in contactos:
    print(f"El teléfono de {consulta} es: {contactos[consulta]}")
else:
    print("El contacto no existe en la agenda.")

print("\n" + "=" * 40 + "\n")

#Punto 5

frase = input("Ingresá una frase: ")
palabras = frase.split()

palabras_unicas = set(palabras)

recuento = {}
for palabra in palabras:
    recuento[palabra] = recuento.get(palabra, 0) + 1

print(f"Palabras_únicas: {palabras_unicas}")
print(f"Recuento: {recuento}")
print("\n" + "=" * 40 + "\n")

#Punto 6

alumnos = {}

print("--- Carga de Alumnos y Notas ---")
for i in range(3):
    nombre = input(f"Nombre del alumno {i+1}: ")
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    n3 = float(input("Nota 3: "))
    alumnos[nombre] = (n1, n2, n3)

print("\n--- Promedios ---")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"El promedio de {nombre} es: {promedio:.2f}")

print("\n" + "=" * 40 + "\n")

#Punto 7

parcial_1 = {
    "Ana",
    "Juan",
    "Carlos",
    "Sofía",
    "Lucía",
} 
parcial_2 = {"Juan", "Sofía", "Pedro", "Mateo", "Carlos"}

ambos = parcial_1 & parcial_2

solo_uno = parcial_1 ^ parcial_2

al_menos_uno = parcial_1 | parcial_2

print(f"Aprobaron ambos: {ambos}")
print(f"Aprobaron solo uno: {solo_uno}")
print(f"Aprobaron al menos uno: {al_menos_uno}")
print("\n" + "=" * 40 + "\n")

#Punto 8

stock_productos = {"remeras": 15, "pantalones": 8, "camperas": 4}

print("Inventario actual:", stock_productos)
producto = input("Ingresá el nombre del producto a gestionar: ").lower()

if producto in stock_productos:
    print(f"El producto ya existe. Stock actual: {stock_productos[producto]}")
    agregar = int(input("¿Cuántas unidades querés agregar?: "))
    stock_productos[producto] += agregar
    print(f"Stock actualizado. Nuevo stock de {producto}: {stock_productos[producto]}")
else:
    print("El producto no existe. Se agregará al inventario.")
    nuevo_stock = int(input(f"Ingresá el stock inicial para {producto}: "))
    stock_productos[producto] = nuevo_stock
    print("Producto agregado con éxito.")

print("Inventario final:", stock_productos)
print("\n" + "=" * 40 + "\n")

#Punto 9

agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "15:00"): "Clase de inglés",
    ("viernes", "18:00"): "Fútbol",
}

print("--- Consulta de Agenda ---")
d = input("Ingresá el día (ej. lunes): ").lower()
h = input("Ingresá la hora (ej. 10:00): ")

clave_busqueda = (d, h)

if clave_busqueda in agenda:
    print(f"Actividad programada: {agenda[clave_busqueda]}")
else:
    print("No hay ninguna actividad registrada en ese día y horario.")

print("\n" + "=" * 40 + "\n")

#Punto 10

paises_capitales = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Uruguay": "Montevideo",
}

capitales_paises = {}

for pais, capital in paises_capitales.items():
    capitales_paises[capital] = pais

print("Diccionario original (País: Capital):", paises_capitales)
print("Diccionario invertido (Capital: País):", capitales_paises)

def separar():
    print("\n" + "=" * 40 + "\n")


# Punto 1

print("Punto 1")
with open("productos.txt", "w") as archivo:
    archivo.write("Lapicera,120.5,30\n")
    archivo.write("Cuaderno,1500.0,15\n")
    archivo.write("Goma,350.75,50\n")
print("Archivo 'productos.txt' creado con éxito.")
separar()


# Punto 2

print("Punto 2")
with open("productos.txt", "r") as archivo:
    for linea in archivo:
        partes = linea.strip().split(",")
        print(
            f"Producto: {partes[0]} | Precio: ${partes[1]} | Cantidad: {partes[2]}"
        )
separar()


# Punto 3

print("Punto 3")
nuevo_nombre = input("Ingresá el nombre del nuevo producto: ")
nuevo_precio = input("Ingresá el precio: ")
nueva_cantidad = input("Ingresá la cantidad: ")

with open("productos.txt", "a") as archivo:
    archivo.write(f"{nuevo_nombre},{nuevo_precio},{nueva_cantidad}\n")
print("Producto agregado correctamente al archivo.")
separar()


# Punto 4

print("Punto 4")
lista_productos = []
with open("productos.txt", "r") as archivo:
    for linea in archivo:
        partes = linea.strip().split(",")
        producto_dict = {
            "nombre": partes[0],
            "precio": float(partes[1]),
            "cantidad": int(partes[2]),
        }
        lista_productos.append(producto_dict)

print("Lista de diccionarios generada:")
for p in lista_productos:
    print(p)
separar()


# Punto 5

print("Punto 5")
busqueda = input("Ingresá el nombre del producto que querés buscar: ")
encontrado = False

for p in lista_productos:
    if p["nombre"].lower() == busqueda.lower():
        print(
            f"¡Encontrado! -> Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}"
        )
        encontrado = True
        break

if not encontrado:
    print("Error: El producto no existe en el registro.")
separar()


# Punto 6

print("Punto 6")
with open("productos.txt", "w") as archivo:
    for p in lista_productos:
        archivo.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")
print("Archivo 'productos.txt' actualizado y sincronizado desde la lista.")
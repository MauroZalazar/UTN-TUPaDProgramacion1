#Punto 1

def imprimir_hola_mundo():
    print("Hola Mundo!")

# Programa principal
imprimir_hola_mundo()

#Punto 2

def saludar_usuario(nombre):
    return f"Hola {nombre}!"

# Programa principal
usuario = input("Ingresá tu nombre: ")
mensaje = saludar_usuario(usuario)
print(mensaje)

#Punto 3

def informacion_personal(nombre, apellido, edad, residencia):
    print(
        f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}."
    )

# Programa principal
n = input("Ingresá tu nombre: ")
a = input("Ingresá tu apellido: ")
e = input("Ingresá tu edad: ")
r = input("Ingresá tu lugar de residencia: ")

informacion_personal(n, a, e, r)

#Punto 4

import math


def calcular_area_circulo(radio):
    return math.pi * (radio**2)


def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

# Programa principal
r = float(input("Ingresá el radio del círculo: "))

area = calcular_area_circulo(r)
perimetro = calcular_perimetro_circulo(r)

print(f"El área es: {area:.2f}")
print(f"El perímetro es: {perimetro:.2f}")

#Punto 5

def segundos_a_horas(segundos):
    return segundos / 3600

# Programa principal
segs = float(input("Ingresá la cantidad de segundos: "))
horas = segundos_a_horas(segs)

print(f"{segs} segundos equivalen a {horas:.2f} horas.")

#Punto 6

def tabla_multiplicar(numero):
    print(f"--- Tabla del {numero} ---")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

# Programa principal
num = int(input("Ingresá un número entero: "))
tabla_multiplicar(num)

#Punto 7

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Error: división por cero"
    return (suma, resta, multiplicacion, division)

# Programa principal
n1 = float(input("Ingresá el primer número: "))
n2 = float(input("Ingresá el segundo número: "))

resultados = operaciones_basicas(n1, n2)
print(f"Resultados (Suma, Resta, Multiplicación, División): {resultados}")

#Punto 8

def calcular_imc(peso, altura):
    return peso / (altura**2)


# Programa principal
p = float(input("Ingresá tu peso en kg (ej. 70.5): "))
alt = float(input("Ingresá tu altura en metros (ej. 1.75): "))

imc = calcular_imc(p, alt)
print(f"Tu Índice de Masa Corporal (IMC) es: {imc:.2f}")

#Punto 9

def celsius_a_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


# Programa principal
c = float(input("Ingresá la temperatura en grados Celsius: "))
f = celsius_a_fahrenheit(c)

print(f"{c}°C equivalen a {f:.2f}°F")

#Punto 10

def calcular_promedio(a, b, c):
    return (a + b + c) / 3


# Programa principal
num1 = float(input("Ingresá el primer número: "))
num2 = float(input("Ingresá el segundo número: "))
num3 = float(input("Ingresá el tercer número: "))

promedio = calcular_promedio(num1, num2, num3)
print(f"El promedio de los tres números es: {promedio:.2f}")
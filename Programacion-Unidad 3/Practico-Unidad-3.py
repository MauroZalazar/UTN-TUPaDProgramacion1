#Punto 1

edad = int(input("Ingrese su edad: "))
if edad > 18:
    print("Es mayor de edad")

#Punto 2

nota = float(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#Punto 3

numero = int(input("Ingrese un número: "))
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

#Punto 4

edad = int(input("Ingrese su edad: "))
if edad < 12:
    print("Niño/a")
elif edad < 18:
    print("Adolescente")
elif edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

#Punto 5

password = input("Ingrese una contraseña: ")
if 8 <= len(password) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#Punto 6

import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

if media > mediana and mediana > moda:
    print("Sesgo positivo o a la derecha")
elif media < mediana and mediana < moda:
    print("Sesgo negativo o a la izquierda")
else:
    print("Sin sesgo")

#Punto 7

texto = input("Ingrese una frase o palabra: ")
if texto.endswith(('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')):
    texto += "!"
print(texto)

#Punto 8

nombre = input("Ingrese su nombre: ")
opcion = int(input("Elija una opción (1: Mayúsculas, 2: Minúsculas, 3: Primera letra mayúscula): "))

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Opción inválida")

#Punto 9

magnitud = float(input("Ingrese la magnitud del terremoto: "))
if magnitud < 3:
    print("Muy leve")
elif magnitud < 4:
    print("Leve")
elif magnitud < 5:
    print("Moderado")
elif magnitud < 6:
    print("Fuerte")
elif magnitud < 7:
    print("Muy Fuerte")
else:
    print("Extremo")

#Punto 10

hemisferio = input("Ingrese el hemisferio (N/S): ").upper()
mes = int(input("Ingrese el número del mes (1-12): "))
dia = int(input("Ingrese el día: "))

if (mes == 12 and dia >= 21) or mes in (1, 2) or (mes == 3 and dia <= 20):
    if hemisferio == 'N':
        print("Invierno")
    else:
        print("Verano")
elif (mes == 3 and dia >= 21) or mes in (4, 5) or (mes == 6 and dia <= 20):
    if hemisferio == 'N':
        print("Primavera")
    else:
        print("Otoño")
elif (mes == 6 and dia >= 21) or mes in (7, 8) or (mes == 9 and dia <= 20):
    if hemisferio == 'N':
        print("Verano")
    else:
        print("Invierno")
else:
    if hemisferio == 'N':
        print("Otoño")
    else:
        print("Primavera")


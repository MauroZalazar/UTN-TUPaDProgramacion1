#Punto 1

print("Hola mundo")

#Punto 2

nombre = input("Ingrese su nombre: ")
print(f"Hola,{nombre}!")

#Punto 3

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su Edad: ")
lugar_de_residencia = input ("Ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido},tengo {edad} años y vivo en {lugar_de_residencia}.")

#Punto 4

import math

radio = float(input("Ingrese el radio del circulo:"))
area = math.pi * (radio ** 2)
perimetro = 2 * math.pi * radio
print(f"Radio: {radio}")
print(f"Area: {area}")
print(f"Perimetro: {perimetro}")

#Punto 5

import math

segundos = float(input("Ingrese la cantidad de segundos: "))
horas = segundos // 3600
print(f"Cantidad de horas: {horas}")

#Punto 6
numero = int(input("Ingrese un numero: "))
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

#Punto 7

def realizar_operaciones():
    print(" Calculadora Básica ")
    
    try:
        
        num1 = int(input("Ingresa el primer número entero (distinto de 0): "))
        num2 = int(input("Ingresa el segundo número entero (distinto de 0): "))

        if num1 == 0 or num2 == 0:
            print("\n Error: Ambos números deben ser distintos de 0.")
            return
                
        suma = num1 + num2
        resta = num1 - num2
        multiplicacion = num1 * num2
        division = num1 / num2  

        print("\n--- Resultados de las Operaciones ---")
        print(f"• Suma ({num1} + {num2}): {suma}")
        print(f"• Resta ({num1} - {num2}): {resta}")
        print(f"• Multiplicación ({num1} * {num2}): {multiplicacion}")
        print(f"• División ({num1} / {num2}): {division:.2f}")

    except ValueError:
        print("\n Error: Debes ingresar un número entero válido.")

if __name__ == "__main__":
    realizar_operaciones()

#Punto 8

def calcular_imc():
    print(" Cálculo de IMC ")
    
    peso = float(input("Ingresa tu peso en kg (ej. 70.5): "))
    altura = float(input("Ingresa tu altura en metros (ej. 1.75): "))
    
    imc = peso / (altura ** 2)
    
    print(f"\nTu Índice de Masa Corporal (IMC) es: {imc:.2f}")

if __name__ == "__main__":
    calcular_imc()

#Punto 9

def convertir_temperatura():
    print(" Conversor de Celsius a Fahrenheit ")
    
    celsius = float(input("Ingresa la temperatura en grados Celsius: "))
    
    fahrenheit = (celsius * 9/5) + 32
    
    print(f"\n{celsius}°C equivalen a {fahrenheit:.2f}°F")

if __name__ == "__main__":
    convertir_temperatura()

#Punto 10

def calcular_promedio():
    print(" Calculadora de Promedio ")
    
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    num3 = float(input("Ingresa el tercer número: "))
    
    promedio = (num1 + num2 + num3) / 3
    
    print(f"\nEl promedio de los tres números es: {promedio:.2f}")

if __name__ == "__main__":
    calcular_promedio()

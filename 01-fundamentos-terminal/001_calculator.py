# Proyecto: Calculadora Simple de Línea de Comandos

# Paso 1: Pidiendo los números al usuario
num1_str = input("Ingresa el primer número: ")
num2_str = input("Ingresa el segundo número: ")

# Paso 2: Pidiendo la operación al usuario
operacion = input("Ingresa la operación (+, -, *, /): ")

# Paso 3: Convirtiendo las entradas a números
try: # Usamos un bloque try-except para manejar posibles errores de conversión
    num1 = float(num1_str)
    num2 = float(num2_str)

    # Paso 4: Realizando la operación según la elección del usuario
    resultado = None # Inicializamos resultado a None

    if operacion == '+':
        resultado = num1 + num2
    elif operacion == '-':
        resultado = num1 - num2
    elif operacion == '*':
        resultado = num1 * num2
    elif operacion == '/':
        if num2 != 0:
            resultado = num1 / num2
        else:
            print("Error: No se puede dividir por cero.")
    else:
        print("Operación no válida.")

    # Paso 5: Mostrando el resultado
    if resultado is not None: # Solo mostramos si resultado tiene un valor (no es None)
         # Puedes usar f-strings para formatear mejor la salida
        print(f"El resultado de {num1} {operacion} {num2} es: {resultado}")

except ValueError:
    print("Error: Por favor, ingresa números válidos.")

    
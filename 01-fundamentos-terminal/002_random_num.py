# Proyecto 2: Juego de Adivinar el Número

# Paso 1: Importamos el módulo random
import random

# Paso 2: La computadora elige un número secreto
numero_secreto = random.randint(1, 100)

# Opcional: Puedes imprimir el número secreto para probar si funciona al principio
# print(f"El número secreto (para prueba) es: {numero_secreto}")

# Variable para guardar el intento del usuario. Inicializamos a un valor que no sea el secreto.
intento = 0
contador_intentos = 0 # Para contar los intentos

print("¡Bienvenido al juego de adivinar el número!")
print("Estoy pensando en un número entre 1 y 100.")

# Paso 3, 4 y 5: El bucle principal del juego, obteniendo el intento y dando pistas
while intento != numero_secreto:
    intento_str = input("Ingresa tu intento: ")

    try:
        intento = int(intento_str) # Convertimos la entrada a entero
        contador_intentos += 1 # Incrementamos el contador en cada intento válido

        # Comparamos el intento con el número secreto y damos pistas
        if intento < numero_secreto:
            print("Demasiado bajo. ¡Intenta de nuevo!")
        elif intento > numero_secreto:
            print("Demasiado alto. ¡Intenta de nuevo!")
        # Si intento == numero_secreto, el bucle termina

    except ValueError:
        print("Entrada no válida. Por favor, ingresa un número entero.")

# Paso 6: Felicitando al usuario (se ejecuta después del bucle)
print(f"¡Felicidades! ¡Adivinaste el número secreto ({numero_secreto})!")
print(f"Te tomó {contador_intentos} intentos.")
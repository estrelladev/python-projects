# Proyecto 3: Generador Simple de Contraseñas Aleatorias

# Paso 1: Importamos los módulos random y string
import random
import string

# Paso 2: Definimos los caracteres posibles para la contraseña
# string.ascii_letters contiene abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
# string.digits contiene 0123456789
caracteres_posibles = string.ascii_letters + string.digits

# Opcional: Puedes añadir símbolos si quieres
# caracteres_posibles = string.ascii_letters + string.digits + string.punctuation

# Paso 3: Pidiendo la longitud deseada al usuario
longitud = 0 # Inicializamos la longitud a 0

try:
    longitud = int(input("Ingresa la longitud deseada para la contraseña: "))

    # Agregamos una pequeña validación para la longitud
    if longitud <= 0:
        print("La longitud debe ser un número positivo.")
        longitud = 0 # Aseguramos que no se genere una contraseña inválida
except ValueError:
    print("Entrada no válida. Por favor, ingresa un número entero.")
    longitud = 0 # Aseguramos que no se genere una contraseña si hay error

# Paso 4 y 5: Generando y mostrando la contraseña (solo si la longitud es válida)
if longitud > 0:
    contrasena_generada = "" # Inicializamos una cadena vacía

    # Usamos un bucle for para elegir caracteres 'longitud' veces
    for _ in range(longitud):
        # Elegimos un carácter aleatorio de los caracteres_posibles
        caracter_aleatorio = random.choice(caracteres_posibles)

        # Añadimos el carácter elegido a nuestra contraseña
        contrasena_generada += caracter_aleatorio

    # Mostramos la contraseña generada
    print("Tu contraseña generada es:", contrasena_generada)
# Proyecto 8: Analizador de Texto Básico

import string # Importamos string para usar string.punctuation (opcional pero útil)
import os # Aunque ya no verificamos existence con os.path.exists, es útil tenerlo importado si quisieras re-agregar esa verificación

# Nombre del archivo de texto a analizar
NOMBRE_ARCHIVO_TEXTO = "text.txt" # <-- Cambiado a text.txt

# Variable para almacenar el contenido del archivo
contenido_texto = ""

# --- LECTURA DEL ARCHIVO ---
try:
    # Abrimos el archivo en modo lectura ('r') con codificación utf-8
    # Usamos 'with' para asegurar que el archivo se cierre
    with open(NOMBRE_ARCHIVO_TEXTO, 'r', encoding='utf-8') as f:
        contenido_texto = f.read() # Leemos todo el contenido del archivo

except FileNotFoundError:
    print(f"Error: El archivo '{NOMBRE_ARCHIVO_TEXTO}' no fue encontrado en la misma carpeta que el script.")
except Exception as e:
    print(f"Error al leer el archivo: {e}")

# --- PROCESAMIENTO Y ANÁLISIS ---
if contenido_texto:
    # 1. Convertir a minúsculas
    texto_procesado = contenido_texto.lower()

    # 2. Eliminar signos de puntuación
    # Podemos usar string.punctuation o definir los nuestros
    # string.punctuation contiene !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    # Puedes añadir o quitar según necesites.
    signos_a_eliminar = string.punctuation + "—" # Añadimos la raya (guion largo) si es necesario

    # Mejor enfoque: reemplazar signos de puntuación y quizás números por espacios
    texto_sin_puntuacion = ""
    for caracter in texto_procesado:
        # Si el caracter es un signo de puntuación O un dígito...
        if caracter in signos_a_eliminar or caracter.isdigit():
            texto_sin_puntuacion += ' ' # Reemplazar por un espacio
        else:
            texto_sin_puntuacion += caracter # Mantener el caracter si no es puntuación/dígito

    # 3. Dividir la cadena en una lista de palabras
    # .split() divide la cadena por cualquier secuencia de espacios en blanco y elimina los vacíos resultantes
    palabras = texto_sin_puntuacion.split()

    # Diccionario para almacenar el conteo de palabras
    conteo_palabras = {}

    # Iteramos sobre la lista de palabras para contarlas
    for palabra in palabras:
        # Solo contamos palabras que no estén vacías (pueden quedar vacías después de la limpieza y split)
        if palabra:
            # Incrementamos el conteo. Si la palabra no existe, get() devuelve 0 y luego sumamos 1.
            conteo_palabras[palabra] = conteo_palabras.get(palabra, 0) + 1

    # --- MOSTRAR RESULTADOS ---
    print("\n--- Análisis del Texto ---")

    # Número total de palabras (contando repeticiones)
    total_palabras = len(palabras)
    print(f"Número total de palabras: {total_palabras}")

    # Número de palabras únicas
    total_palabras_unicas = len(conteo_palabras)
    print(f"Número de palabras únicas: {total_palabras_unicas}")

    # Frecuencia de cada palabra
    print("\n--- Frecuencia de Palabras ---")
    # Opcional: ordenar por frecuencia (más común primero)
    # sorted_items = sorted(conteo_palabras.items(), key=lambda item: item[1], reverse=True)
    # for palabra, conteo in sorted_items:
    #      print(f"'{palabra}': {conteo}")
    # O solo iterar sobre los elementos del diccionario en su orden original:
    for palabra, conteo in conteo_palabras.items():
         print(f"'{palabra}': {conteo}")

else:
    # Este mensaje se muestra si el archivo estaba vacío o hubo error al leerlo (el error ya se imprimió antes)
    print("No hay contenido para analizar.")
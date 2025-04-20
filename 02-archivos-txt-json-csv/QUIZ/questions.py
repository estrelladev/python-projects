# Proyecto 9: Juego de Preguntas y Respuestas desde Archivo

import os

# Nombre del archivo con las preguntas
NOMBRE_ARCHIVO_PREGUNTAS = "questions.txt" # <-- Cambiado a questions.txt

# Lista para almacenar las preguntas (cada pregunta será un diccionario)
preguntas_quiz = []

def cargar_preguntas(nombre_archivo):
    """Carga las preguntas desde el archivo de texto."""
    preguntas_cargadas = []
    if not os.path.exists(nombre_archivo):
        print(f"Error: El archivo '{nombre_archivo}' no fue encontrado en la misma carpeta que el script.")
        return preguntas_cargadas # Devolvemos lista vacía

    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as f:
            lineas = f.readlines() # Leemos todas las líneas

        pregunta_actual = {}
        opciones_actuales = []
        # Procesamos las líneas para construir las preguntas
        for i, linea in enumerate(lineas):
            linea_limpia = linea.strip() # Quitamos espacios al inicio/final y saltos de línea

            if not linea_limpia: # Si la línea está vacía, significa que terminó una pregunta
                # Si tenemos datos de una pregunta incompleta, la guardamos
                if pregunta_actual:
                     # Antes de guardar, verificamos si tiene los componentes mínimos esperados
                    if "pregunta" in pregunta_actual and opciones_actuales and "respuesta" in pregunta_actual:
                        pregunta_actual["opciones"] = opciones_actuales
                        preguntas_cargadas.append(pregunta_actual)
                    else:
                        # Opcional: Mostrar advertencia si una pregunta parece incompleta
                        # print(f"Advertencia: Pregunta incompleta antes de la línea {i+1}. Ignorada.")
                        pass # No mostramos advertencia por ahora para mantener la terminal limpia

                    # Reiniciamos para la siguiente pregunta
                    pregunta_actual = {}
                    opciones_actuales = []
                continue # Pasamos a la siguiente línea

            # Si la línea no está vacía, intentamos identificar qué parte de la pregunta es
            if not pregunta_actual:
                # La primera línea no vacía después de un espacio es la pregunta
                pregunta_actual["pregunta"] = linea_limpia
            elif linea_limpia.upper().startswith("RESPUESTA:"): # Hacemos la comparación en mayúsculas por flexibilidad
                # Línea de respuesta correcta
                # Quitamos prefijos "Respuesta:" o "RESPUESTA:", limpiamos espacios y convertimos a mayúsculas
                respuesta = linea_limpia.replace("Respuesta:", "").replace("RESPUESTA:", "").strip().upper()
                pregunta_actual["respuesta"] = respuesta
            else:
                # Las otras líneas son opciones
                opciones_actuales.append(linea_limpia)

        # Después del bucle, verificamos si quedó una última pregunta incompleta
        if pregunta_actual:
             if "pregunta" in pregunta_actual and opciones_actuales and "respuesta" in pregunta_actual:
                 pregunta_actual["opciones"] = opciones_actuales
                 preguntas_cargadas.append(pregunta_actual)
             # else:
                 # Opcional: Mostrar advertencia si la última pregunta parece incompleta
                 # print(f"Advertencia: Última pregunta incompleta. Ignorada.")
                 pass # No mostramos advertencia por ahora


        print(f"Cargadas {len(preguntas_cargadas)} preguntas desde {nombre_archivo}.")
        return preguntas_cargadas

    except Exception as e:
        print(f"Error al leer o procesar el archivo de preguntas: {e}")
        return [] # Devolvemos lista vacía en caso de error


# --- Programa principal ---
print("¡Bienvenido al Juego de Quiz!")

# Cargar las preguntas al iniciar
preguntas_quiz = cargar_preguntas(NOMBRE_ARCHIVO_PREGUNTAS)

# Verificamos si se cargaron preguntas
if not preguntas_quiz:
    print("No se pudieron cargar las preguntas del quiz o el archivo estaba vacío. Terminando.")
    exit() # Salimos del programa si no hay preguntas

# Inicializamos el contador de puntuación
puntuacion = 0

# Bucle para jugar cada pregunta
for num_pregunta, pregunta_dicc in enumerate(preguntas_quiz):
    print(f"\n--- Pregunta #{num_pregunta + 1} ---")
    # Mostramos el texto de la pregunta (con get por seguridad, aunque debería existir)
    print(pregunta_dicc.get("pregunta", "Texto de pregunta no disponible"))

    # Mostramos las opciones (iteramos sobre la lista 'opciones' en el diccionario)
    opciones = pregunta_dicc.get("opciones", []) # Obtenemos la lista de opciones, por defecto lista vacía si no existe
    if opciones:
        for opcion in opciones:
            print(opcion)
    else:
        print("Opciones no disponibles.")

    # Pedimos la respuesta al usuario
    # Limpiamos espacios, convertimos a mayúsculas
    respuesta_usuario = input("Tu respuesta (ej: A, B, C, D): ").strip().upper()

    # Verificamos la respuesta
    # Obtenemos la respuesta correcta del diccionario, limpiamos espacios, convertimos a mayúsculas
    respuesta_correcta = pregunta_dicc.get("respuesta", "").strip().upper()

    if respuesta_usuario and respuesta_usuario == respuesta_correcta:
        print("¡Correcto!")
        puntuacion += 1 # Incrementamos la puntuación si es correcta
    else:
        # Mostramos la respuesta correcta si la respuesta del usuario es incorrecta o no válida
        if respuesta_correcta: # Solo mostramos la respuesta correcta si estaba especificada en el archivo
             print(f"Incorrecto. La respuesta correcta era: {respuesta_correcta}")
        else:
             print("Incorrecto. La respuesta correcta no estaba especificada en el archivo.")


# --- Fin del Quiz ---
print("\n--- Fin del Quiz ---")
print(f"Tu puntuación final es: {puntuacion} de {len(preguntas_quiz)}")
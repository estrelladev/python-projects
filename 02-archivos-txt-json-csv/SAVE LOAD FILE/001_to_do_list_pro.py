# Proyecto 6: Gestor Simple de Lista de Tareas con Guardado y Carga

import os

# Nombre del archivo donde se guardarán las tareas
NOMBRE_ARCHIVO = "tareas.txt"

# Nuestra lista para almacenar las tareas
lista_tareas = []

def cargar_tareas(lista, nombre_archivo):
    """Carga las tareas desde el archivo."""
    # Verificamos si el archivo existe antes de intentar leerlo
    if os.path.exists(nombre_archivo):
        try:
            # Usamos 'with' para abrir el archivo en modo lectura ('r').
            # Si open() falla (ej: permisos, etc.), el 'except' lo capturará.
            with open(nombre_archivo, 'r') as f:
                # Leemos cada línea del archivo
                for linea in f:
                    # Eliminamos los espacios en blanco (incluido el salto de línea '\n') al final de la línea
                    tarea = linea.strip()
                    # Si la línea no está vacía después de strip, la agregamos a la lista
                    if tarea:
                        lista.append(tarea)
            print(f"Tareas cargadas desde {nombre_archivo}.")
        except Exception as e: # Captura cualquier error general al leer el archivo
            print(f"Error al cargar tareas desde {nombre_archivo}: {e}")
    else:
        print(f"El archivo {nombre_archivo} no existe. Comenzando con lista vacía.")


def guardar_tareas(lista, nombre_archivo):
    """Guarda las tareas en el archivo."""
    try:
        # Usamos 'with' para abrir el archivo en modo escritura ('w').
        # Esto sobrescribe el archivo si ya existe o crea uno nuevo.
        # Si open() falla al escribir (ej: disco lleno, permisos), el 'except' lo capturará.
        with open(nombre_archivo, 'w') as f:
            # Iteramos sobre cada tarea en la lista
            for tarea in lista:
                # Escribimos la tarea seguida de un salto de línea '\n'
                f.write(tarea + '\n')
        # print(f"Tareas guardadas en {nombre_archivo}.") # Puedes comentar si no quieres el mensaje cada vez
    except Exception as e: # Captura cualquier error general al escribir en el archivo
        print(f"Error al guardar tareas en {nombre_archivo}: {e}")


def agregar_tarea(lista):
    """Pide al usuario una tarea y la agrega a la lista."""
    tarea = input("Ingresa la nueva tarea: ")
    if tarea: # Aseguramos que la tarea no esté vacía
        lista.append(tarea)
        print(f"Tarea '{tarea}' agregada.")
        return True # Indicamos que se agregó una tarea
    else:
        print("No se puede agregar una tarea vacía.")
        return False # Indicamos que no se agregó tarea


def ver_tareas(lista):
    """Muestra todas las tareas en la lista, numeradas."""
    print("\n--- Tus Tareas ---")
    if not lista:
        print("No hay tareas en la lista.")
    else:
        # Usamos enumerate para obtener el índice y la tarea al mismo tiempo
        for indice, tarea in enumerate(lista):
            print(f"{indice + 1}. {tarea}") # Mostramos índice + 1 para que empiece desde 1 para el usuario


def marcar_completada(lista):
    """Pide al usuario el número de tarea y la marca como completada."""
    if not lista:
        print("No hay tareas para marcar.")
        return False # Indicamos que no se hizo cambio

    ver_tareas(lista) # Mostramos las tareas primero para que el usuario sepa qué número elegir

    try:
        numero_tarea_str = input("Ingresa el número de la tarea a marcar como completada: ")
        numero_tarea = int(numero_tarea_str)
        indice_tarea = numero_tarea - 1 # Convertimos el número del usuario a índice de lista (restamos 1)

        # Verificamos si el índice es válido
        if 0 <= indice_tarea < len(lista):
            # Verificamos si ya está marcada para evitar duplicados
            if not lista[indice_tarea].startswith("[Completada]"):
                lista[indice_tarea] = f"[Completada] {lista[indice_tarea]}"
                print(f"Tarea {numero_tarea} marcada como completada.")
                return True # Indicamos que se hizo un cambio
            else:
                print(f"La tarea {numero_tarea} ya estaba marcada como completada.")
                return False # No hubo cambio
        else:
            print("Número de tarea no válido.")
            return False # No hubo cambio

    except ValueError:
        print("Entrada no válida. Por favor, ingresa un número entero.")
        return False # No hubo cambio
    except IndexError: # Aunque la validación de índice lo previene, es buena práctica
        # Este error no debería ocurrir con la validación 'if 0 <= indice_tarea < len(lista):'
        print("Error interno: Índice fuera de rango inesperado.")
        return False # No hubo cambio


# --- Programa principal ---
print("¡Bienvenido a tu Gestor Simple de Lista de Tareas!")

# Cargar las tareas al iniciar el programa
cargar_tareas(lista_tareas, NOMBRE_ARCHIVO)

# Bucle principal del programa
while True:
    print("\n--- Menú ---")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Marcar tarea como completada")
    print("4. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == '1':
        # Llamamos a la función y verificamos si agregó una tarea válida
        if agregar_tarea(lista_tareas):
             guardar_tareas(lista_tareas, NOMBRE_ARCHIVO) # GUARDAR solo si se agregó correctamente
    elif opcion == '2':
        ver_tareas(lista_tareas)
    elif opcion == '3':
        # Llamamos a la función y verificamos si marcó una tarea correctamente
        if marcar_completada(lista_tareas):
             guardar_tareas(lista_tareas, NOMBRE_ARCHIVO) # GUARDAR solo si se marcó correctamente
    elif opcion == '4':
        print("¡Adiós!")
        # No es estrictamente necesario guardar aquí si guardamos después de cada modificación exitosa.
        # Si no guardaras después de cada modificación, DEBERÍAS LLAMAR A guardar_tareas() AQUÍ antes del break.
        break # Salimos del bucle while True
    else:
        print("Opción no válida. Intenta de nuevo.")
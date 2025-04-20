# Proyecto 4: Gestor Simple de Lista de Tareas (con funciones)

# Nuestra lista para almacenar las tareas (variable global para simplicidad inicial)
lista_tareas = []

def agregar_tarea(lista):
    """Pide al usuario una tarea y la agrega a la lista."""
    tarea = input("Ingresa la nueva tarea: ")
    if tarea: # Aseguramos que la tarea no esté vacía
        lista.append(tarea)
        print(f"Tarea '{tarea}' agregada.")
    else:
        print("No se puede agregar una tarea vacía.")


def ver_tareas(lista):
    """Muestra todas las tareas en la lista, numeradas."""
    print("\n--- Tus Tareas ---")
    if not lista:
        print("No hay tareas en la lista.")
    else:
        for indice, tarea in enumerate(lista):
            print(f"{indice + 1}. {tarea}")


def marcar_completada(lista):
    """Pide al usuario el número de tarea y la marca como completada."""
    if not lista:
        print("No hay tareas para marcar.")
        return # Salimos de la función si la lista está vacía

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
            else:
                 print(f"La tarea {numero_tarea} ya estaba marcada como completada.")
        else:
            print("Número de tarea no válido.")

    except ValueError:
        print("Entrada no válida. Por favor, ingresa un número entero.")
    except IndexError: # Aunque la validación de índice lo previene, es buena práctica
        print("Error interno: Índice fuera de rango inesperado.") # Este error no debería ocurrir con la validación anterior


# --- Programa principal ---
print("¡Bienvenido a tu Gestor Simple de Lista de Tareas!")

# Bucle principal del programa
while True:
    print("\n--- Menú ---")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Marcar tarea como completada")
    print("4. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == '1':
        agregar_tarea(lista_tareas) # Llamamos a la función
    elif opcion == '2':
        ver_tareas(lista_tareas) # Llamamos a la función
    elif opcion == '3':
        marcar_completada(lista_tareas) # Llamamos a la función
    elif opcion == '4':
        print("¡Adiós!")
        break # Salimos del bucle while True
    else:
        print("Opción no válida. Intenta de nuevo.")
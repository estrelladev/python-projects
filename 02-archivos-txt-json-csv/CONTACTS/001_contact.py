# Proyecto 7: Agenda de Contactos Simple con Archivo JSON

import json # Importamos el módulo json para trabajar con archivos JSON
import os   # Importamos os para verificar si el archivo existe

# Nombre del archivo donde se guardarán los contactos
NOMBRE_ARCHIVO = "contactos.json"

# Nuestra lista para almacenar los contactos. Cada contacto será un diccionario.
agenda = []

def cargar_contactos(lista, nombre_archivo):
    """Carga los contactos desde el archivo JSON."""
    if os.path.exists(nombre_archivo):
        try:
            with open(nombre_archivo, 'r') as f:
                # json.load() lee el archivo JSON y lo convierte a un objeto Python (en este caso, una lista)
                datos_cargados = json.load(f)
                # Aseguramos que lo cargado sea una lista antes de asignarla
                if isinstance(datos_cargados, list):
                    lista.extend(datos_cargados) # Usamos extend para añadir los elementos a la lista existente
                    print(f"Contactos cargados desde {nombre_archivo}.")
                else:
                    print(f"El archivo {nombre_archivo} no contiene una lista válida de contactos.")
        except json.JSONDecodeError:
            print(f"Error: El archivo {nombre_archivo} no es un archivo JSON válido.")
        except Exception as e:
            print(f"Error al cargar contactos desde {nombre_archivo}: {e}")
    else:
        print(f"El archivo {nombre_archivo} no existe. Comenzando con agenda vacía.")

def guardar_contactos(lista, nombre_archivo):
    """Guarda los contactos en el archivo JSON."""
    try:
        with open(nombre_archivo, 'w') as f:
            # json.dump() convierte un objeto Python (nuestra lista de diccionarios) a formato JSON y lo escribe en el archivo
            json.dump(lista, f, indent=4) # indent=4 hace que el archivo sea más legible con indentación de 4 espacios
        # print(f"Contactos guardados en {nombre_archivo}.") # Opcional
    except Exception as e:
        print(f"Error al guardar contactos en {nombre_archivo}: {e}")


def agregar_contacto(lista):
    """Pide los datos de un contacto y lo agrega a la lista."""
    print("\n--- Agregar Nuevo Contacto ---")
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    email = input("Email: ")

    # Verificamos que al menos el nombre no esté vacío
    if nombre.strip(): # Usamos strip() para considerar nombres con solo espacios como vacíos
        nuevo_contacto = {
            "nombre": nombre.strip(), # Guardamos el nombre sin espacios al inicio/final
            "telefono": telefono.strip(),
            "email": email.strip()
        }
        lista.append(nuevo_contacto)
        print(f"Contacto '{nombre.strip()}' agregado.")
        return True # Indicamos que se agregó
    else:
        print("El nombre del contacto no puede estar vacío.")
        return False # Indicamos que no se agregó

def ver_contactos(lista):
    """Muestra todos los contactos en la lista."""
    print("\n--- Tus Contactos ---")
    if not lista:
        print("No hay contactos en la agenda.")
    else:
        # Usamos enumerate para numerar los contactos
        for indice, contacto in enumerate(lista):
            print(f"\nContacto {indice + 1}:")
            # Iteramos sobre los pares clave-valor del diccionario de cada contacto
            # Usamos .get() por seguridad, aunque sabemos que estas claves existen si se agregaron correctamente
            print(f"  Nombre: {contacto.get('nombre', 'N/A')}")
            print(f"  Teléfono: {contacto.get('telefono', 'N/A')}")
            print(f"  Email: {contacto.get('email', 'N/A')}")


def buscar_contacto(lista):
    """Busca contactos por nombre."""
    print("\n--- Buscar Contacto ---")
    termino_busqueda = input("Ingresa el nombre a buscar: ").strip().lower() # Convertimos a minúsculas y quitamos espacios para búsqueda

    if not termino_busqueda:
        print("Ingresa un nombre para buscar.")
        return

    contactos_encontrados = []

    # Iteramos sobre la lista de contactos
    for contacto in lista:
        # Verificamos si el nombre del contacto (en minúsculas, quitando espacios) contiene el término de búsqueda
        if termino_busqueda in contacto.get("nombre", "").strip().lower():
            contactos_encontrados.append(contacto) # Si coincide, lo añadimos a la lista de encontrados

    if not contactos_encontrados:
        print(f"No se encontraron contactos con el nombre '{termino_busqueda}'.")
    else:
        print("\n--- Contactos Encontrados ---")
        # Usamos la misma lógica de ver_contactos para mostrar los encontrados
        for indice, contacto in enumerate(contactos_encontrados):
             print(f"\nContacto Encontrado {indice + 1}:")
             print(f"  Nombre: {contacto.get('nombre', 'N/A')}")
             print(f"  Teléfono: {contacto.get('telefono', 'N/A')}")
             print(f"  Email: {contacto.get('email', 'N/A')}")


def eliminar_contacto(lista):
    """Pide el número de contacto y lo elimina."""
    if not lista:
        print("No hay contactos para eliminar.")
        return False # Indicamos que no se hizo cambio

    ver_contactos(lista) # Mostrar contactos para que el usuario sepa qué número elegir

    try:
        numero_contacto_str = input("Ingresa el número del contacto a eliminar: ")
        numero_contacto = int(numero_contacto_str)
        indice_contacto = numero_contacto - 1 # Convertir a índice (base 0)

        # Validar el índice
        if 0 <= indice_contacto < len(lista):
            # Eliminamos el contacto de la lista usando pop()
            contacto_eliminado = lista.pop(indice_contacto)
            print(f"Contacto '{contacto_eliminado.get('nombre', 'N/A')}' eliminado.")
            return True # Indicamos que se eliminó
        else:
            print("Número de contacto no válido.")
            return False

    except ValueError:
        print("Entrada no válida. Por favor, ingresa un número entero.")
        return False
    except IndexError: # Aunque la validación anterior lo previene, es buena práctica
         print("Error interno: Índice fuera de rango inesperado.")
         return False


# --- Programa principal ---
print("¡Bienvenido a tu Agenda de Contactos!")

# Cargar contactos al iniciar
cargar_contactos(agenda, NOMBRE_ARCHIVO)

# Bucle principal del programa
while True:
    print("\n--- Menú de Agenda ---")
    print("1. Agregar contacto")
    print("2. Ver contactos")
    print("3. Buscar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == '1':
        # Llamamos a la función y verificamos si agregó un contacto válido
        if agregar_contacto(agenda):
            guardar_contactos(agenda, NOMBRE_ARCHIVO) # GUARDAR solo si se agregó correctamente
    elif opcion == '2':
        ver_contactos(agenda)
    elif opcion == '3':
        buscar_contacto(agenda)
    elif opcion == '4':
        # Llamamos a la función y verificamos si eliminó un contacto correctamente
        if eliminar_contacto(agenda):
             guardar_contactos(agenda, NOMBRE_ARCHIVO) # GUARDAR solo si se eliminó correctamente
    elif opcion == '5':
        print("¡Adiós!")
        # No es estrictamente necesario guardar aquí si guardamos después de cada modificación exitosa.
        # Si no guardaras después de cada modificación, DEBERÍAS LLAMAR A guardar_contactos() AQUÍ antes del break.
        break # Salimos del bucle while True
    else:
        print("Opción no válida. Intenta de nuevo.")
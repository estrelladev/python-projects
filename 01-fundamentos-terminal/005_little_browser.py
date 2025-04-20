# Proyecto 5: Buscador Básico de Información de Países (con función)

# Datos de ejemplo (un diccionario donde cada clave es un país y el valor es otro diccionario con sus datos)
datos_paises = {
    "Mexico": {
        "Capital": "Ciudad de México",
        "Continente": "América del Norte",
        "Poblacion": "Aprox. 128 millones"
    },
    "Canada": {
        "Capital": "Ottawa",
        "Continente": "América del Norte",
        "Poblacion": "Aprox. 38 millones"
    },
    "España": {
        "Capital": "Madrid",
        "Continente": "Europa",
        "Poblacion": "Aprox. 47 millones"
    },
    "Japon": {
        "Capital": "Tokio",
        "Continente": "Asia",
        "Poblacion": "Aprox. 126 millones"
    }
    # Puedes añadir más países aquí
}

def buscar_pais(nombre_pais, datos):
    """Busca un país en los datos y muestra su información."""
    # Normalizamos la entrada del usuario (primera letra mayúscula, resto minúsculas)
    # para intentar que coincida con las claves de nuestro diccionario
    pais_formateado = nombre_pais.capitalize()

    # Verificamos si el país formateado existe como clave en nuestro diccionario
    if pais_formateado in datos:
        info_pais = datos[pais_formateado]

        print(f"\n--- Información de {pais_formateado} ---")
        # Iteramos sobre los pares clave-valor del diccionario de información del país
        for clave, valor in info_pais.items():
            print(f"{clave}: {valor}")

    else:
        print(f"Información de '{nombre_pais}' no encontrada. Intenta con otro país.")

# --- Programa principal ---
print("¡Bienvenido al Buscador Básico de Información de Países!")
print("Datos disponibles para: " + ", ".join(datos_paises.keys())) # Opcional: mostrar países disponibles al inicio

# Bucle principal de búsqueda
while True:
    print("\n--- Buscar País ---")
    pais_a_buscar = input("Ingresa el nombre del país a buscar (o escribe 'salir' para terminar): ")

    # Quitamos espacios en blanco al inicio/final y convertimos a minúsculas para verificar si quiere salir
    if pais_a_buscar.strip().lower() == 'salir':
        print("¡Adiós!")
        break
    elif pais_a_buscar.strip() == "": # Manejar entrada vacía
        print("Por favor, ingresa un nombre de país.")
        continue # Volver al inicio del bucle
    else:
        # Llamamos a la función de búsqueda
        buscar_pais(pais_a_buscar, datos_paises)
# Proyecto 10: Procesador Básico de Datos desde CSV (Análisis de Eventos Históricos)

import csv # Importamos el módulo csv
import os # Importamos el módulo os para verificar la existencia del archivo

# Nombre del archivo CSV a procesar
NOMBRE_ARCHIVO_CSV = "datos.csv" # Asegúrate de que este archivo exista con el contenido que proporcionaste

# --- LECTURA DEL ARCHIVO CSV ---
datos_leidos = [] # Lista para almacenar los datos leídos (cada fila será una lista de cadenas)

try:
    # Verificamos si el archivo existe
    if not os.path.exists(NOMBRE_ARCHIVO_CSV):
         print(f"Error: El archivo '{NOMBRE_ARCHIVO_CSV}' no fue encontrado en la misma carpeta que el script.")
    else:
        # Usamos 'with' para abrir el archivo. 'r' para lectura, newline='' es importante para CSV.
        # encoding='utf-8' para caracteres especiales.
        with open(NOMBRE_ARCHIVO_CSV, mode='r', newline='', encoding='utf-8') as f:
            # Creamos un objeto lector de CSV
            lector_csv = csv.reader(f)

            # Iteramos sobre cada fila en el archivo CSV
            for fila in lector_csv:
                datos_leidos.append(fila) # Añadimos la fila (que es una lista de cadenas) a nuestra lista principal

        print(f"Leídas {len(datos_leidos)} filas desde {NOMBRE_ARCHIVO_CSV}.")
        # print("Datos leídos (para verificación):", datos_leidos) # Opcional para verificar

except Exception as e:
    print(f"Error general al leer el archivo CSV: {e}")

# --- PROCESAMIENTO Y ANÁLISIS DE DATOS ---

encabezado = []
datos_filas = [] # Lista para almacenar solo las filas de datos (sin el encabezado)

if datos_leidos: # Solo procesamos si se leyeron datos
    encabezado = datos_leidos[0] # La primera lista es el encabezado
    datos_filas = datos_leidos[1:] # Todas las filas desde la segunda en adelante son los datos

    # Opcional: Imprimir encabezado y primeras filas de datos para verificar
    # print("\nEncabezado:", encabezado)
    # print("Primeras filas de datos:", datos_filas[:5]) # Mostrar las primeras 5 filas

    if datos_filas: # Solo procedemos si hay filas de datos después del encabezado
        print("\n--- Análisis de Eventos Históricos ---")

        # 1. Contar el número total de eventos
        total_eventos = len(datos_filas)
        print(f"Número total de eventos registrados: {total_eventos}")

        # 2. Listar todos los eventos
        print("\n--- Lista de Eventos ---")
        try:
            # Intentamos encontrar el índice de la columna 'Evento'
            indice_evento = encabezado.index("Evento")
            eventos_encontrados = True
        except ValueError:
            print("Error: No se encontró la columna 'Evento' en el encabezado.")
            eventos_encontrados = False

        if eventos_encontrados:
             if total_eventos > 0:
                for i, fila in enumerate(datos_filas):
                    if len(fila) > indice_evento: # Asegurarse de que la fila tiene suficientes columnas
                         print(f"- {fila[indice_evento]}")
                    else:
                         print(f"- [Evento sin nombre en fila {i + 2}]")
             else:
                  print("No hay eventos para listar.")


        # 3. Contar eventos por categoría
        print("\n--- Conteo de Eventos por Categoría ---")
        conteo_por_categoria = {} # Diccionario para almacenar el conteo

        try:
            # Intentamos encontrar el índice de la columna 'Categoría'
            indice_categoria = encabezado.index("Categoría")
            categoria_encontrada = True
        except ValueError:
            print("Error: No se encontró la columna 'Categoría' en el encabezado.")
            categoria_encontrada = False


        if categoria_encontrada:
            if total_eventos > 0:
                for i, fila in enumerate(datos_filas):
                    if len(fila) > indice_categoria: # Asegurarse de que la fila tiene suficientes columnas
                        categoria = fila[indice_categoria].strip() # Obtener la categoría y limpiar espacios
                        if categoria: # Solo contar si la categoría no está vacía
                            # Usamos get() para incrementar el conteo
                            conteo_por_categoria[categoria] = conteo_por_categoria.get(categoria, 0) + 1
                        else:
                             print(f"Advertencia: Categoría vacía en fila {i + 2}.")
                    else:
                         print(f"Advertencia: Fila {i + 2} no tiene suficiente columnas para la categoría.")

                # Mostrar el conteo por categoría
                if conteo_por_categoria:
                    # Opcional: ordenar por nombre de categoría o por conteo
                    for categoria, conteo in sorted(conteo_por_categoria.items()): # Ordenado por nombre de categoría
                        print(f"- {categoria}: {conteo}")
                else:
                     print("No se encontraron categorías válidas.")

            else:
                 print("No hay datos para categorizar.")
        else:
            print("No se puede categorizar sin la columna 'Categoría'.")


        # Puedes añadir más análisis aquí, por ejemplo:
        # - Contar eventos por país
        # - Encontrar eventos de un país específico
        # - Encontrar el evento más antiguo o más reciente (requiere parsing de fechas, un poco más avanzado)


    else:
         print("El archivo CSV solo contiene encabezado, no hay datos de eventos para procesar.")

elif not datos_leidos:
    # Este mensaje se muestra si el archivo no pudo ser leído o estaba vacío al inicio
    # El error específico de FileNotFoundError u otro ya se imprimió antes
    print("No se leyeron datos del archivo CSV.")
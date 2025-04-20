# --- Proyecto 2: Introducción a Pandas - Exploración de Eventos WWII ---

# Paso 3.2: Importar Pandas
import pandas as pd
print("Pandas importado exitosamente!")
print("-" * 40)

# Nombre del archivo CSV con eventos de la WWII
nombre_archivo = "datos.csv"

# Paso 3.3: Cargar Datos desde CSV
try:
    # Intentamos cargar el CSV en un DataFrame
    # parse_dates=['Fecha'] intenta convertir la columna 'Fecha' a tipo datetime
    df_eventos_ww2 = pd.read_csv(nombre_archivo, encoding='utf-8', parse_dates=['Fecha'])
    print(f"Archivo '{nombre_archivo}' cargado exitosamente en un DataFrame.")

except FileNotFoundError:
    print(f"Error CRÍTICO: No se encontró el archivo '{nombre_archivo}'.")
    print("Asegúrate de que esté en la misma carpeta que este script.")
    exit() # Salimos si no se puede cargar el archivo
except Exception as e:
    print(f"Ocurrió un error al leer el archivo CSV con parse_dates: {e}")
    # Si falla parse_dates, intentamos cargar sin él:
    try:
        print("Intentando cargar de nuevo sin parsear fechas automáticamente...")
        df_eventos_ww2 = pd.read_csv(nombre_archivo, encoding='utf-8')
        print("Archivo cargado, pero la columna 'Fecha' podría ser de tipo texto (object).")
        print("La ordenación por fecha podría ser alfabética en lugar de cronológica.")
    except Exception as e2:
         print(f"Error CRÍTICO definitivo al cargar el archivo: {e2}")
         exit()

print("-" * 40)

# Solo continuamos si df_eventos_ww2 se cargó correctamente
if 'df_eventos_ww2' in locals() and isinstance(df_eventos_ww2, pd.DataFrame):

    # Paso 3.4: Exploración Básica del DataFrame
    print("\n--- Primeros 5 Eventos (head) ---")
    print(df_eventos_ww2.head())

    print("\n--- Últimos 3 Eventos (tail) ---")
    print(df_eventos_ww2.tail(3))

    num_filas, num_columnas = df_eventos_ww2.shape
    print(f"\n--- Dimensiones ---")
    print(f"El DataFrame tiene {num_filas} filas (eventos) y {num_columnas} columnas.")

    print("\n--- Nombres de Columnas ---")
    print(list(df_eventos_ww2.columns))

    print("\n--- Información General (info) ---")
    # Muestra índice, columnas, conteo de no nulos, tipo de dato (Dtype), uso de memoria
    df_eventos_ww2.info()

    print("\n--- Estadísticas Descriptivas para columnas de Texto (describe object) ---")
    # Muestra: count(conteo), unique(valores únicos), top(valor más frecuente), freq(frecuencia del top)
    print(df_eventos_ww2.describe(include='object'))
    # Si tuvieras columnas numéricas (ej. 'Año' numérico), podrías usar df_eventos_ww2.describe()

    print("-" * 40)

    # Paso 3.5: Seleccionar Datos
    print("\n--- Selección: Columna 'Evento' (como Series, primeras 5) ---")
    columna_evento = df_eventos_ww2['Evento']
    print(columna_evento.head())

    print("\n--- Selección: Columnas 'Evento', 'País', 'Fecha' (como DataFrame, primeras 5) ---")
    columnas_seleccionadas = df_eventos_ww2[['Evento', 'País', 'Fecha']]
    print(columnas_seleccionadas.head())

    print("\n--- Selección: Primeros 3 eventos (filas 0 a 2 por slicing) ---")
    primeros_tres_eventos = df_eventos_ww2[0:3]
    print(primeros_tres_eventos)

    print("-" * 40)

    # --- Sección "Plus" para Destacar ---

    # Plus 4.1: Cargar Solo Columnas Específicas (Ejemplo)
    print("\n--- [Plus] Ejemplo: Cargar solo 'Evento', 'Fecha', 'Resultado' ---")
    try:
        df_columnas_utiles = pd.read_csv(
            nombre_archivo,
            encoding='utf-8',
            usecols=['Evento', 'Fecha', 'Resultado'], # Lista de columnas a cargar
            parse_dates=['Fecha']
        )
        print("DataFrame solo con columnas útiles (primeras 5 filas):")
        print(df_columnas_utiles.head())
    except Exception as e:
        print(f"Error al cargar columnas específicas: {e}")

    print("-" * 40)

    # Plus 4.2: Contar Valores Únicos (Value Counts)
    print("\n--- [Plus] Conteo de Eventos por Categoría ---")
    # Muestra cuántas veces aparece cada categoría de evento
    conteo_categorias = df_eventos_ww2['Categoría'].value_counts()
    print(conteo_categorias)

    print("\n--- [Plus] Conteo por entrada en la columna 'País' ---")
    # Muestra cuántas veces aparece cada combinación única en la columna 'País'
    # Ojo: "Alemania/Polonia" cuenta como una entrada única diferente de "Alemania"
    conteo_pais_entrada = df_eventos_ww2['País'].value_counts()
    print(conteo_pais_entrada)

    print("-" * 40)

    # Plus 4.3: Ordenar el DataFrame
    print("\n--- [Plus] Eventos Ordenados por Fecha (primeros 5) ---")
    # ascending=True para orden cronológico (más antiguo primero)
    # na_position='last' pone filas con fecha desconocida (NaN) al final
    try:
        df_ordenado_fecha = df_eventos_ww2.sort_values(by='Fecha', ascending=True, na_position='last')
        print(df_ordenado_fecha.head())
    except TypeError as e:
        print(f"No se pudo ordenar por fecha (posiblemente no es tipo datetime): {e}")
        print("Mostrando ordenado por 'Evento' en su lugar:")
        df_ordenado_evento = df_eventos_ww2.sort_values(by='Evento')
        print(df_ordenado_evento.head())


    # Ejemplo de orden descendente por Fecha (más reciente primero)
    # print("\n--- [Plus] Eventos Ordenados por Fecha (Descendente, primeros 5) ---")
    # df_ordenado_fecha_desc = df_eventos_ww2.sort_values(by='Fecha', ascending=False, na_position='last')
    # print(df_ordenado_fecha_desc.head())

else:
     print("No se pudo cargar el DataFrame. El script no puede continuar con el análisis.")

print("\n--- Fin del Script de Exploración Pandas ---")
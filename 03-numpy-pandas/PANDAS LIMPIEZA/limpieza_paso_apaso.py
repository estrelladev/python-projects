# --- Proyecto 3: Limpieza Paso a Paso ---

# Paso 1: Configuración Inicial y Carga

import pandas as pd
import numpy as np # Lo podríamos necesitar luego

# Define el nombre del archivo (asegúrate que esté en esta carpeta)
nombre_archivo = "datos.csv"

print(">>> PASO 1: Cargando el DataFrame...")
try:
    # Cargamos SIN parse_dates esta vez, lo haremos manualmente después
    df_eventos_ww2 = pd.read_csv(nombre_archivo, encoding='utf-8')
    print(f"Archivo '{nombre_archivo}' cargado exitosamente.")
    print("\nInformación inicial del DataFrame (df_eventos_ww2.info()):")
    df_eventos_ww2.info()

except FileNotFoundError:
    print(f"Error CRÍTICO: No se encontró el archivo '{nombre_archivo}'.")
    print("Asegúrate de que esté en la misma carpeta que este script.")
    exit()
except Exception as e:
    print(f"Error CRÍTICO al cargar {nombre_archivo}: {e}")
    exit()

print("-" * 50)
# --- Fin Paso 1 ---

# --- Añadir al final del script ---

# Paso 2: Detectar Nulos y Duplicados (Comprobación)

print("\n>>> PASO 2: Verificando Nulos y Duplicados...")

# Detectar Nulos por columna
print("\nConteo de valores nulos por columna:")
print(df_eventos_ww2.isnull().sum())

# Detectar Filas Duplicadas Completas
num_duplicados = df_eventos_ww2.duplicated().sum()
print(f"\nNúmero total de filas duplicadas encontradas: {num_duplicados}")

# Comentario: Como esperábamos (y vimos en el .info()), no hay nulos ni duplicados
# en este dataset inicial. Pero estos comandos son esenciales para datasets reales.

print("-" * 50)
# --- Fin Paso 2 ---

# --- Añadir al final del script ---

# Paso 3: Convertir Tipo de Dato de 'Fecha'

print("\n>>> PASO 3: Convirtiendo la columna 'Fecha' a tipo datetime...")

# Guardamos el tipo ANTES de convertir para comparar
tipo_antes = df_eventos_ww2['Fecha'].dtype
print(f"Tipo de 'Fecha' ANTES de convertir: {tipo_antes}")

# Intentamos la conversión. errors='coerce' es CLAVE aquí.
# Hará que las fechas inválidas (como '1939-1945') se conviertan en NaT (Not a Time)
df_eventos_ww2['Fecha'] = pd.to_datetime(df_eventos_ww2['Fecha'], errors='coerce')

# Verificamos el tipo DESPUÉS
tipo_despues = df_eventos_ww2['Fecha'].dtype
print(f"Tipo de 'Fecha' DESPUÉS de convertir: {tipo_despues}")

# Comprobamos si se generaron NaT (valores nulos de fecha)
nats_en_fecha = df_eventos_ww2['Fecha'].isnull().sum()
print(f"\nNúmero de fechas no convertibles (ahora son NaT): {nats_en_fecha}")

# Mostramos las filas donde la fecha es NaT para ver cuál falló
print("\nFilas donde 'Fecha' es NaT:")
# df_eventos_ww2['Fecha'].isnull() devuelve True para las filas con NaT
print(df_eventos_ww2[df_eventos_ww2['Fecha'].isnull()])

# Volvemos a ver la información general para confirmar el cambio de tipo en 'Fecha'
print("\nInformación del DataFrame DESPUÉS de convertir 'Fecha' (df_eventos_ww2.info()):")
df_eventos_ww2.info()


print("-" * 50)
# --- Fin Paso 3 ---

# --- Añadir al final del script ---

# Paso 4: Ordenar Cronológicamente

print("\n>>> PASO 4: Ordenando el DataFrame por la 'Fecha' (datetime)...")

# Ahora que 'Fecha' es datetime, sort_values funcionará cronológicamente.
# na_position='last' es buena práctica para poner los NaT al final.
df_ordenado_crono = df_eventos_ww2.sort_values(by='Fecha', ascending=True, na_position='last')

print("\nPrimeros 5 eventos ordenados cronológicamente:")
# Mostramos solo Evento y Fecha para claridad
print(df_ordenado_crono[['Evento', 'Fecha']].head())

print("\nÚltimos 5 eventos ordenados cronológicamente (incluye NaT al final):")
print(df_ordenado_crono[['Evento', 'Fecha']].tail())

print("-" * 50)
# --- Fin Paso 4 ---

# --- Añadir al final del script ---

# Paso 5: Filtrado de Datos (Selección por Condiciones)

print("\n>>> PASO 5: Filtrando el DataFrame por condiciones...")

# 1. Filtrar para obtener solo eventos de categoría 'Batalla clave'
# Creamos una condición booleana: df_eventos_ww2['Categoría'] == 'Batalla clave'
# Usamos esa condición dentro de los corchetes [] para seleccionar las filas donde es True
print("\nFiltrado 1: Eventos de Categoría 'Batalla clave'")
batallas_clave = df_eventos_ww2[df_eventos_ww2['Categoría'] == 'Batalla clave']
# Mostramos las columnas relevantes del resultado
print(batallas_clave[['Evento', 'Categoría', 'País']])

# 2. Filtrar eventos donde 'País' contiene la palabra 'Alemania'
# Usamos el accesor .str y el método contains()
# na=False es importante por si hubiera valores NaN en la columna 'País' (evita errores)
print("\nFiltrado 2: Eventos donde 'País' contiene 'Alemania'")
eventos_alemania = df_eventos_ww2[df_eventos_ww2['País'].str.contains('Alemania', na=False)]
print(eventos_alemania[['Evento', 'País']])

# 3. Filtrar combinando condiciones:
# Queremos eventos cuya 'Categoría' contenga 'Batalla' Y ('&')
# cuyo 'País' contenga 'Japón'.
# ¡OJO con los paréntesis alrededor de cada condición individual!
print("\nFiltrado 3: Batallas ('Categoría' contiene 'Batalla') Y ('&') Involucran a Japón ('País' contiene 'Japón')")
batallas_japon = df_eventos_ww2[
    (df_eventos_ww2['Categoría'].str.contains('Batalla', na=False)) &
    (df_eventos_ww2['País'].str.contains('Japón', na=False))
]
print(batallas_japon[['Evento', 'Categoría', 'País']])


print("-" * 50)
# --- Fin Paso 5 ---

# --- Añadir al final del script ---

# Paso 6: Renombrar Columnas

print("\n>>> PASO 6: Renombrando columnas para mayor claridad...")

# Mostramos los nombres ANTES de renombrar
print("Nombres de columnas ANTES:", list(df_eventos_ww2.columns))

# Usamos el método .rename() y le pasamos un diccionario
# { 'nombre_viejo': 'nombre_nuevo', ... } dentro del argumento 'columns'
# IMPORTANTE: .rename() devuelve un NUEVO DataFrame con los cambios.
# Debemos reasignarlo a nuestra variable df_eventos_ww2 para que los cambios persistan.
df_eventos_ww2 = df_eventos_ww2.rename(columns={
    'País': 'Paises_Involucrados',
    'Resultado': 'Descripcion_Resultado'
})

# Mostramos los nombres DESPUÉS de renombrar para verificar
print("Nombres de columnas DESPUÉS:", list(df_eventos_ww2.columns))

# Alternativa (menos común, modifica el DataFrame directamente):
# df_eventos_ww2.rename(columns={'País': 'Paises_Involucrados', 'Resultado': 'Descripcion_Resultado'}, inplace=True)
# Generalmente se prefiere la reasignación por claridad.

print("-" * 50)
# --- Fin Paso 6 ---

# --- Añadir al final del script ---

# Paso 7: Manipulación de Texto (Plus)

print("\n>>> PASO 7: Manipulando texto en columnas...")

# 1. Convertir una columna de texto a minúsculas
# Usamos .str para acceder a métodos de string para toda la columna
print("\nConvirtiendo 'Descripcion_Resultado' a minúsculas (primeras 5):")
# Aplicamos el cambio directamente a la columna
df_eventos_ww2['Descripcion_Resultado'] = df_eventos_ww2['Descripcion_Resultado'].str.lower()
print(df_eventos_ww2['Descripcion_Resultado'].head())

# 2. Dividir texto de una columna
# Vamos a intentar dividir la columna 'Paises_Involucrados' usando '/' como separador
# Esto es útil si quisiéramos analizar los países individualmente más tarde.
print("\nDividiendo 'Paises_Involucrados' por '/' (devuelve listas, primeras 5):")
# El resultado de .str.split() es una Serie donde cada elemento es una LISTA de strings
paises_split = df_eventos_ww2['Paises_Involucrados'].str.split('/')
print(paises_split.head())

# Nota: Para trabajar con esas listas (ej. contar cada país individualmente),
# se necesitarían pasos adicionales como el método .explode() de Pandas,
# que es un poco más avanzado pero muy potente.

print("-" * 50)
# --- Fin Paso 7 ---

# --- Añadir al final del script ---

# Paso 8: Crear Columna 'Año' desde Fecha (Plus)

print("\n>>> PASO 8: Creando una nueva columna 'Año'...")

# Es buena práctica verificar que la columna 'Fecha' es de tipo datetime
# antes de intentar usar el accesor .dt
if pd.api.types.is_datetime64_any_dtype(df_eventos_ww2['Fecha']):
    # Si es datetime, usamos .dt.year para extraer el año
    df_eventos_ww2['Año'] = df_eventos_ww2['Fecha'].dt.year

    # Mostramos algunas columnas, incluida la nueva 'Año', para verificar
    print("\nDataFrame con la nueva columna 'Año' (primeras 5 filas):")
    print(df_eventos_ww2[['Evento', 'Fecha', 'Año']].head())

    # Verificamos el tipo de dato de la nueva columna 'Año'
    # Será float64 si contiene NaN (porque NaT en Fecha -> NaN en Año)
    # O podría ser Int64 si no hubiera NaNs o si lo convirtiéramos explícitamente
    print("\nTipo de dato de la columna 'Año':", df_eventos_ww2['Año'].dtype)

    # Opcional: Convertir a tipo Int64 que permite enteros Y NaN (más limpio que float)
    # df_eventos_ww2['Año'] = df_eventos_ww2['Año'].astype('Int64')
    # print("Tipo de dato de 'Año' después de convertir a Int64:", df_eventos_ww2['Año'].dtype)
    # print("\nDataFrame con 'Año' como Int64 (primeras 5 filas):")
    # print(df_eventos_ww2[['Evento', 'Fecha', 'Año']].head())

    # Veamos la fila del Holocausto para ver el NaN/NA en Año
    print("\nFila del Holocausto mostrando NaN/<NA> en Año:")
    print(df_eventos_ww2[df_eventos_ww2['Evento'] == 'Holocausto'][['Evento', 'Fecha', 'Año']])

else:
    print("\nNo se pudo crear la columna 'Año' porque 'Fecha' no es de tipo datetime.")


print("-" * 50)
# --- Fin Paso 8 ---

print("\n¡PROCESO DE LIMPIEZA Y PREPARACIÓN COMPLETADO!")
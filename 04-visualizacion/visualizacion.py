import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("Bibliotecas de visualización importadas.")

# --- Carga y Limpieza Esencial (adaptado del Proyecto 3) ---
nombre_archivo = "datos.csv" # Asegúrate que sea el archivo expandido
try:
    df_eventos_ww2 = pd.read_csv(nombre_archivo, encoding='utf-8')
    print(f"Archivo '{nombre_archivo}' cargado.")

    # Convertir Fecha a datetime (manejo de errores)
    df_eventos_ww2['Fecha'] = pd.to_datetime(df_eventos_ww2['Fecha'], errors='coerce')

    # Crear columna 'Año'
    if pd.api.types.is_datetime64_any_dtype(df_eventos_ww2['Fecha']):
        df_eventos_ww2['Año'] = df_eventos_ww2['Fecha'].dt.year
        # >>> IMPORTANTE para gráficos basados en año:
        # >>> Eliminar filas donde el año no se pudo determinar (Fecha es NaT)
        # >>> y convertir Año a entero para mejor visualización en ejes.
        df_eventos_ww2.dropna(subset=['Año'], inplace=True) # inplace=True modifica el DF directamente
        df_eventos_ww2['Año'] = df_eventos_ww2['Año'].astype(int)
        print("Columna 'Año' creada y limpiada (NaNs eliminados, tipo entero).")
    else:
        print("Columna 'Fecha' no se pudo convertir a datetime, no se creó 'Año'.")
        exit() # Salimos si no tenemos año

    # Renombrar columnas (opcional pero bueno tenerlo consistente)
    df_eventos_ww2 = df_eventos_ww2.rename(columns={
        'País': 'Paises_Involucrados',
        'Resultado': 'Descripcion_Resultado'
    })
    # Limpiar duplicados (ya que sabemos que hay uno)
    df_eventos_ww2.drop_duplicates(inplace=True)
    print("Filas duplicadas eliminadas.")
    print("Datos listos para visualización.")

except Exception as e:
    print(f"Error durante la carga o preparación: {e}")
    exit()
print("-" * 50)
# --- Fin Carga y Limpieza ---

# Ahora 'df_eventos_ww2' contiene los datos limpios y listos

print("\n>>> Gráfico 1: Conteo de Eventos por Categoría...")
plt.figure(figsize=(10, 8)) # Ajustar tamaño para mejor legibilidad

# Usamos Seaborn countplot. 'y' para categorías en eje vertical (mejor si son largas)
# 'order' para ordenar las barras de más frecuente a menos frecuente
sns.countplot(
    data=df_eventos_ww2,
    y='Categoría',
    order=df_eventos_ww2['Categoría'].value_counts().index # Ordena por frecuencia
)

plt.title('Número de Eventos Registrados por Categoría WWII')
plt.xlabel('Número de Eventos') # Etiqueta eje X
plt.ylabel('Categoría del Evento') # Etiqueta eje Y
plt.tight_layout() # Ajusta el layout para evitar solapamientos
plt.savefig('ww2_eventos_por_categoria.png') # Guarda el gráfico (Plus)
plt.show() # Muestra el gráfico
print("Gráfico 'ww2_eventos_por_categoria.png' guardado.")
print("-" * 50)

print("\n>>> Gráfico 2: Conteo de Eventos por Año...")
plt.figure(figsize=(12, 6)) # Tamaño de la figura

# countplot para el número de eventos en cada año
sns.countplot(data=df_eventos_ww2, x='Año', color='skyblue') # 'color' para elegir un color

plt.title('Número de Eventos Registrados por Año WWII (1938-1945)')
plt.xlabel('Año')
plt.ylabel('Número de Eventos')
plt.xticks(rotation=45) # Rotar etiquetas del eje X si se solapan
plt.tight_layout()
plt.savefig('ww2_eventos_por_año_barras.png') # Guarda el gráfico
plt.show()
print("Gráfico 'ww2_eventos_por_año_barras.png' guardado.")
print("-" * 50)

print("\n>>> Gráfico 3 (Plus): Tendencia de Eventos por Año (Línea)...")

# 1. Calcular cuántos eventos hay por año
# value_counts() cuenta, sort_index() ordena por año (el índice)
eventos_por_año = df_eventos_ww2['Año'].value_counts().sort_index()

# 2. Crear el gráfico de línea
plt.figure(figsize=(12, 6))
# Usamos Matplotlib directamente aquí. plot(x, y)
plt.plot(eventos_por_año.index, eventos_por_año.values, marker='o', linestyle='-') # 'marker' y 'linestyle' para estilo

plt.title('Tendencia del Número de Eventos Registrados por Año WWII')
plt.xlabel('Año')
plt.ylabel('Número de Eventos')
# plt.grid(True) # Añadir una cuadrícula si se desea
plt.xticks(eventos_por_año.index) # Asegura que todos los años aparezcan en el eje X
plt.tight_layout()
plt.savefig('ww2_eventos_por_año_linea.png') # Guarda el gráfico
plt.show()
print("Gráfico 'ww2_eventos_por_año_linea.png' guardado.")
print("-" * 50)

print("\n>>> Gráfico 4 (Plus): Eventos por Año con Matplotlib (Barras)...")

# Ya calculamos 'eventos_por_año' en el paso anterior
plt.figure(figsize=(12, 6))

# Usamos plt.bar(x, height)
plt.bar(eventos_por_año.index, eventos_por_año.values, color='lightcoral')

plt.title('Número de Eventos Registrados por Año WWII (Matplotlib)')
plt.xlabel('Año')
plt.ylabel('Número de Eventos')
plt.xticks(eventos_por_año.index) # Asegura que todos los años aparezcan en el eje X
plt.tight_layout()
plt.savefig('ww2_eventos_por_año_barras_mpl.png') # Guarda el gráfico
plt.show()
print("Gráfico 'ww2_eventos_por_año_barras_mpl.png' guardado.")
print("-" * 50)
# --- Mini-Proyecto NumPy Adaptado: Bajas WWII ---

# Importamos la biblioteca NumPy
import numpy as np

# Definimos las etiquetas para claridad (opcional, no parte del array NumPy)
potencias = ["Alemania", "URSS", "Reino Unido", "EE.UU."]
anios = ["1941", "1943", "1945"] # Representan periodos/años clave

# 1. Crear el array 2D de bajas (en millones)
# Filas: Alemania, URSS, UK, USA
# Columnas: '41, '43, '45 (estimados)
bajas_ww2 = np.array([
    [1.2, 3.0, 2.5],  # Alemania
    [2.0, 5.5, 4.0],  # URSS
    [0.2, 0.4, 0.3],  # Reino Unido
    [0.1, 0.6, 0.5]   # EE.UU.
])

print("--- Datos Iniciales (Bajas Estimadas en Millones) ---")
print("Array de Bajas WWII:\n", bajas_ww2)
print("Forma (potencias, años):", bajas_ww2.shape)
print("-" * 30) # Separador visual

# 2. Calcular el total de bajas por potencia (suma de cada fila, axis=1)
# axis=1 suma los elementos a lo largo de las columnas para cada fila.
total_por_potencia = np.sum(bajas_ww2, axis=1)
print("Total Bajas Estimadas por Potencia (Ale, URSS, UK, USA):", total_por_potencia)
# Opcional: Mostrar con etiquetas
# for i, potencia in enumerate(potencias):
#    print(f"- {potencia}: {total_por_potencia[i]:.1f} millones")
print("-" * 30)

# 3. Calcular el total de bajas por año (suma de cada columna, axis=0)
# axis=0 suma los elementos a lo largo de las filas para cada columna.
total_por_anio = np.sum(bajas_ww2, axis=0)
print("Total Bajas Estimadas por Año ('41, '43, '45):", total_por_anio)
# Opcional: Mostrar con etiquetas
# for i, anio in enumerate(anios):
#     print(f"- {anio}: {total_por_anio[i]:.1f} millones")
print("-" * 30)

# 4. Encontrar la cifra más alta y más baja en la tabla
# Sin especificar 'axis', la operación se aplica a todo el array.
max_bajas_periodo = np.max(bajas_ww2)
min_bajas_periodo = np.min(bajas_ww2)
print(f"Máxima cifra de bajas en un periodo/potencia: {max_bajas_periodo} millones")
print(f"Mínima cifra de bajas en un periodo/potencia: {min_bajas_periodo} millones")
print("-" * 30)

# 5. (Plus) Ajustar todas las estimaciones multiplicando por 1.1 usando broadcasting
factor_ajuste = 1.1
bajas_ajustadas = bajas_ww2 * factor_ajuste
print("--- Resultados con Ajuste (x 1.1) ---")
print("Bajas Ajustadas:\n", bajas_ajustadas)
print("-" * 30)

# 6. (Plus) Reformar (reshape) las bajas ajustadas a un único vector 1D
bajas_ajustadas_1d = bajas_ajustadas.reshape(-1) # -1 aplana el array
print("Bajas Ajustadas en formato 1D (aplanado):", bajas_ajustadas_1d)
print("Forma del array 1D:", bajas_ajustadas_1d.shape)
print("-" * 30)
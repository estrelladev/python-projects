# --- Proyecto 5: Regresión Lineal Simple con Scikit-learn (WWII Impacto vs Año) ---

# Paso 4.2: Imports
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split # Para dividir datos
from sklearn.linear_model import LinearRegression  # El modelo de Regresión Lineal
from sklearn.metrics import mean_squared_error, r2_score # Métricas de evaluación
import matplotlib.pyplot as plt # Para graficar (Plus)
import seaborn as sns           # Para graficar (Plus) - aunque no lo usemos tanto aquí

print("Bibliotecas para ML importadas.")
print("-" * 50)

# Paso 4.3: Cargar y Preparar Datos (Esencial)

# --- Carga y Limpieza Mínima ---
nombre_archivo = "datos.csv" # El que AHORA incluye 'Impacto'
try:
    df_eventos_ww2 = pd.read_csv(nombre_archivo, encoding='utf-8')
    print(f"Archivo '{nombre_archivo}' cargado.")

    # 1. Convertir Fecha y crear Año (manejando NaT)
    df_eventos_ww2['Fecha'] = pd.to_datetime(df_eventos_ww2['Fecha'], errors='coerce')
    if pd.api.types.is_datetime64_any_dtype(df_eventos_ww2['Fecha']):
        df_eventos_ww2['Año'] = df_eventos_ww2['Fecha'].dt.year
    else:
        raise ValueError("Columna Fecha no se pudo convertir a datetime.")

    # 2. Asegurar que 'Impacto' sea numérico (coerce errores a NaN)
    df_eventos_ww2['Impacto'] = pd.to_numeric(df_eventos_ww2['Impacto'], errors='coerce')

    # 3. Eliminar filas donde 'Año' o 'Impacto' sean NaN
    rows_before = len(df_eventos_ww2)
    df_eventos_ww2.dropna(subset=['Año', 'Impacto'], inplace=True)
    rows_after = len(df_eventos_ww2)
    print(f"Eliminadas {rows_before - rows_after} filas con NaN en 'Año' o 'Impacto'.")

    # 4. Convertir 'Año' a entero
    df_eventos_ww2['Año'] = df_eventos_ww2['Año'].astype(int)

    # 5. Eliminar duplicados (basado en todas las columnas)
    rows_before_dedup = len(df_eventos_ww2)
    df_eventos_ww2.drop_duplicates(inplace=True)
    rows_after_dedup = len(df_eventos_ww2)
    print(f"Eliminadas {rows_before_dedup - rows_after_dedup} filas duplicadas.")


    print("Datos listos para Machine Learning.")
    print(f"Tamaño final del DataFrame: {df_eventos_ww2.shape}")
    print("Tipos de datos relevantes:")
    # Usamos .info() en una selección para ver solo lo relevante
    df_eventos_ww2[['Año', 'Impacto']].info()


except Exception as e:
    print(f"Error durante la carga o preparación para ML: {e}")
    exit()
print("-" * 50)
# --- Fin Carga y Limpieza Mínima ---


# Paso 4.4: Definir Características (X) y Objetivo (y)
print("\n>>> Definiendo Características (X) y Objetivo (y)...")
# Intentaremos predecir 'Impacto' (y) basándonos solo en 'Año' (X).
X = df_eventos_ww2[['Año']] # DataFrame 2D para X
y = df_eventos_ww2['Impacto']   # Serie 1D para y

print("Forma de X:", X.shape)
print("Forma de y:", y.shape)
print("\nPrimeras filas de X:")
print(X.head())
print("\nPrimeras filas de y:")
print(y.head())
print("-" * 50)


# Paso 4.5: Dividir Datos en Entrenamiento y Prueba
print("\n>>> Dividiendo datos en Entrenamiento (70%) y Prueba (30%)...")
# test_size=0.3 -> 30% para prueba
# random_state=42 -> para reproducibilidad
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

print("Tamaño de X_train:", X_train.shape)
print("Tamaño de X_test:", X_test.shape)
print("Tamaño de y_train:", y_train.shape)
print("Tamaño de y_test:", y_test.shape)
print("-" * 50)


# Paso 4.6: Crear y Entrenar el Modelo de Regresión Lineal
print("\n>>> Creando y Entrenando el Modelo de Regresión Lineal...")
modelo_lr = LinearRegression() # Crear instancia
modelo_lr.fit(X_train, y_train) # Entrenar con datos de entrenamiento
print("¡Modelo entrenado exitosamente!")
print("-" * 50)


# Paso 4.7: Realizar Predicciones sobre el conjunto de Prueba
print("\n>>> Realizando predicciones sobre el conjunto de Prueba (X_test)...")
y_pred = modelo_lr.predict(X_test) # Predecir usando el modelo entrenado

print("\nComparación rápida (primeros 5 valores de prueba):")
print("Valores Reales (y_test): ", y_test.values[:5])
print("Valores Predichos (y_pred):", np.round(y_pred[:5], 2))
print("-" * 50)


# Paso 4.8: Evaluar el rendimiento del Modelo
print("\n>>> Evaluando el rendimiento del Modelo...")
mse = mean_squared_error(y_test, y_pred) # Error Cuadrático Medio
rmse = np.sqrt(mse)                      # Raíz del Error Cuadrático Medio
r2 = r2_score(y_test, y_pred)            # Coeficiente de Determinación R²

print(f"Error Cuadrático Medio (MSE):           {mse:.2f}")
print(f"Raíz del Error Cuadrático Medio (RMSE): {rmse:.2f}")
print(f"Coeficiente de Determinación (R²):      {r2:.2f}")
# Nota: Un R² bajo (cercano a 0 o negativo) indica que el 'Año' por sí solo
# explica muy poco de la variación en el 'Impacto' de los eventos. ¡Lo cual es esperable!
print("-" * 50)


# Paso 4.9: Inspeccionar el Modelo Aprendido
print("\n>>> Inspeccionando el Modelo Aprendido (y = w*Año + b)...")
# Coeficiente (w, la pendiente para 'Año')
print(f"Coeficiente (w) para 'Año': {modelo_lr.coef_[0]:.4f}")
# Intercepto (b)
print(f"Intercepto (b):             {modelo_lr.intercept_:.4f}")
print("-" * 50)


# --- Sección "Plus" ---

# Plus 5.1: Visualizar la Regresión Lineal
print("\n>>> [Plus] Visualizando la Regresión Lineal...")
plt.figure(figsize=(10, 6))
plt.scatter(X_test, y_test, color='cornflowerblue', label='Datos Reales (Prueba)', alpha=0.7) # Puntos reales
plt.plot(X_test, y_pred, color='firebrick', linewidth=2, label='Línea de Regresión (Predicción)') # Línea del modelo
plt.title('Regresión Lineal: Impacto del Evento WWII vs Año')
plt.xlabel('Año')
plt.ylabel('Impacto Estimado (1-10)')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('ww2_regresion_impacto_año.png') # Guardar
plt.show() # Mostrar
print("Gráfico 'ww2_regresion_impacto_año.png' guardado.")
print("-" * 50)


# Plus 5.2: Predecir el impacto para un año específico
print("\n>>> [Plus] Prediciendo el impacto para un año específico (ej: 1943)...")
año_nuevo = pd.DataFrame({'Año': [1943]}) # Crear DataFrame para la predicción
prediccion_nueva = modelo_lr.predict(año_nuevo)
print(f"Predicción de impacto para el año {año_nuevo['Año'].iloc[0]}: {prediccion_nueva[0]:.2f}")
print("-" * 50)


print("\n¡PROYECTO 5 (INTRO ML) COMPLETADO!")
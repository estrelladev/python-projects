import cv2
import os # Importamos os para manejar rutas de archivos

# --- Configuración ---
# Ruta al archivo XML del clasificador Haar Cascade
# Asegúrate de que esta ruta sea correcta o que el archivo esté en la misma carpeta
# Si está en la misma carpeta, solo necesitas el nombre del archivo.
ruta_cascada = 'haarcascade_frontalface_default.xml'

# Ruta a la imagen donde quieres detectar caras
ruta_imagen = 'mi_foto.png'
# --- Comprobaciones Previas ---
# Verificar si el archivo de cascada existe
if not os.path.exists(ruta_cascada):
    print(f"Error: No se encontró el archivo clasificador en '{ruta_cascada}'")
    print("Asegúrate de haber descargado 'haarcascade_frontalface_default.xml' y que la ruta sea correcta.")
    exit()

# Verificar si la imagen existe
if not os.path.exists(ruta_imagen):
    print(f"Error: No se encontró la imagen en '{ruta_imagen}'")
    print("Por favor, verifica la ruta de la imagen.")
    exit()

# --- Carga y Procesamiento ---
# Cargar el clasificador Haar Cascade para detección de caras
face_cascade = cv2.CascadeClassifier(ruta_cascada)

# Leer la imagen de entrada
imagen = cv2.imread(ruta_imagen)

# Verificar si la imagen se cargó correctamente
if imagen is None:
    print(f"Error: No se pudo cargar la imagen desde '{ruta_imagen}'")
    print("Verifica que el archivo no esté corrupto y sea un formato de imagen válido.")
    exit()

# Convertir la imagen a escala de grises (Haar Cascade funciona mejor en escala de grises)
imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# --- Detección de Caras ---
# Detectar caras en la imagen
# detectMultiScale(imagen, scaleFactor, minNeighbors)
# - scaleFactor: Qué tanto se reduce el tamaño de la imagen en cada escala. Un valor más bajo (ej. 1.05) es más lento pero detecta más caras. Un valor común es 1.1 o 1.2.
# - minNeighbors: Cuántos vecinos debe tener cada rectángulo candidato para retenerlo. Un valor más alto (ej. 5 o 6) resulta en menos detecciones pero de mayor calidad (menos falsos positivos).
caras = face_cascade.detectMultiScale(
    imagen_gris,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30) # Tamaño mínimo del objeto a detectar (en píxeles)
)

print(f"Se encontraron {len(caras)} cara(s) en la imagen.")

# --- Dibujar Rectángulos ---
# Dibujar un rectángulo alrededor de cada cara detectada
# Las 'caras' son una lista de tuplas (x, y, w, h)
# x, y: Coordenada superior izquierda del rectángulo
# w: Ancho del rectángulo
# h: Alto del rectángulo
for (x, y, w, h) in caras:
    # Dibuja el rectángulo en la imagen original (a color)
    # cv2.rectangle(imagen, punto_inicio, punto_final, color_BGR, grosor_linea)
    cv2.rectangle(imagen, (x, y), (x+w, y+h), (0, 255, 0), 2) # Verde (BGR), grosor 2

# --- Mostrar Resultado ---
# Mostrar la imagen con las caras detectadas
cv2.imshow('Caras Detectadas', imagen)

# Esperar a que el usuario presione una tecla para cerrar la ventana
print("Presiona cualquier tecla para cerrar la ventana de la imagen...")
cv2.waitKey(0)

# Liberar recursos y cerrar todas las ventanas de OpenCV
cv2.destroyAllWindows()
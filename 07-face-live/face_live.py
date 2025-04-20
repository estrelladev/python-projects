import cv2
import os

# --- Configuración ---
# Ruta al archivo XML del clasificador Haar Cascade
# Asegúrate de que esté en la misma carpeta o la ruta sea correcta
ruta_cascada = 'haarcascade_frontalface_default.xml'

# --- Comprobaciones Previas ---
# Verificar si el archivo de cascada existe
if not os.path.exists(ruta_cascada):
    print(f"Error: No se encontró el archivo clasificador en '{ruta_cascada}'")
    print("Asegúrate de haber descargado 'haarcascade_frontalface_default.xml' y que esté en la misma carpeta que este script.")
    exit()

# --- Carga ---
# Cargar el clasificador Haar Cascade
face_cascade = cv2.CascadeClassifier(ruta_cascada)

# --- Inicializar Webcam ---
# Iniciar la captura de video desde la cámara web predeterminada (índice 0)
# Si tienes varias cámaras, puedes probar con 1, 2, etc.
cap = cv2.VideoCapture(0)

# Verificar si la cámara se abrió correctamente
if not cap.isOpened():
    print("Error: No se pudo abrir la cámara web.")
    print("Asegúrate de que no esté siendo usada por otra aplicación y que tengas los permisos necesarios.")
    exit()

print("Iniciando detección en tiempo real...")
print(">>> Presiona la tecla 'q' (minúscula) en la ventana de la cámara para salir <<<")

# --- Bucle Principal ---
while True:
    # Leer un frame (fotograma) de la cámara
    ret, frame = cap.read()

    # Si no se pudo leer el frame (ej. cámara desconectada), salir del bucle
    if not ret:
        print("Error: No se pudo leer el frame de la cámara. Saliendo...")
        break

    # Convertir el frame a escala de grises
    frame_gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar caras en el frame gris
    caras = face_cascade.detectMultiScale(
        frame_gris,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30) # Puedes ajustar este tamaño mínimo
    )

    # Dibujar rectángulos alrededor de las caras detectadas en el frame original (a color)
    for (x, y, w, h) in caras:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2) # Rectángulo verde

    # Mostrar el frame con las detecciones
    # Puedes cambiar el título de la ventana si quieres
    cv2.imshow('Deteccion de Caras - Webcam (Presiona q para salir)', frame)

    # Esperar 1 milisegundo y verificar si se presionó la tecla 'q' para salir
    # El `& 0xFF` es una máscara necesaria en sistemas de 64 bits
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Tecla 'q' presionada. Saliendo del programa...")
        break

# --- Limpieza ---
# Liberar el objeto de captura de video
print("Liberando cámara...")
cap.release()
# Cerrar todas las ventanas de OpenCV
print("Cerrando ventanas.")
cv2.destroyAllWindows()
print("Programa finalizado.")
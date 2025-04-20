# Módulo 7: Reconocimiento Facial (Video en Vivo)

Este módulo extiende las técnicas de detección facial aprendidas en el módulo anterior para aplicarlas en tiempo real a un flujo de video capturado desde una cámara web.

## Proyectos del Módulo

* **Detección de Caras en Vivo:** (`face_live.py`) - Captura video de la cámara, detecta caras en cada fotograma y muestra el resultado en tiempo real.
    * *Documentación detallada:* `README.md` *(a crear)*

## Conceptos Clave del Módulo

* Acceder y capturar video desde la cámara web (`cv2.VideoCapture`).
* Leer fotogramas (frames) del flujo de video (`cap.read()`).
* Procesar video fotograma a fotograma dentro de un bucle (`while True`).
* Aplicar la detección facial (conversión a gris, `detectMultiScale`, dibujar rectángulos) a cada fotograma.
* Mostrar el video procesado en una ventana (`cv2.imshow`).
* Manejar la salida del bucle (e.g., al presionar una tecla específica con `cv2.waitKey`).
* Liberar los recursos de la cámara y cerrar ventanas (`cap.release()`, `cv2.destroyAllWindows`).

---

[Volver al Índice Principal](../README.md)
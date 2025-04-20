# Módulo 6: Reconocimiento Facial (Imagen)

Introducción a la Visión por Computadora (Computer Vision) utilizando la librería OpenCV. Este módulo se enfoca específicamente en la tarea de detectar rostros humanos dentro de imágenes estáticas utilizando clasificadores pre-entrenados (Haar Cascades).

## Proyectos del Módulo

* **Detección de Caras en Imagen:** (`face.py`) - Carga una imagen y dibuja rectángulos alrededor de las caras detectadas.
    * *Documentación detallada:* `README.md` *(a crear)*

## Conceptos Clave del Módulo

* Importar y usar OpenCV (`import cv2`).
* Cargar imágenes (`cv2.imread`).
* Convertir imágenes a escala de grises (`cv2.cvtColor`).
* Cargar clasificadores Haar Cascade (`cv2.CascadeClassifier`).
* Detectar objetos (caras) en imágenes (`cascade.detectMultiScale`).
* Parámetros de `detectMultiScale` (`scaleFactor`, `minNeighbors`, `minSize`).
* Dibujar formas sobre imágenes (`cv2.rectangle`).
* Mostrar imágenes en ventanas (`cv2.imshow`, `cv2.waitKey`, `cv2.destroyAllWindows`).

---

[Volver al Índice Principal](../README.md)
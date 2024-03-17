from PyQt5 import QtWidgets, uic, QtGui, QtCore
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QImage
import cv2
import time
import numpy as np
# Iniciar la aplicación
app = QtWidgets.QApplication([])

# Cargar archivos .ui
window = uic.loadUi("Procesamiento_digital_de_imágenes.ui")

filename = None
final_image = None

def cargarImagen():
    global filename
    filename, _ = QFileDialog.getOpenFileName(filter="Image (*.*)")
    if filename:
        imagen = cv2.imread(filename)
        setPhoto(imagen)

def cargarImagen_gray():
    global filename, final_image
    if filename:
        final_image = cv2.imread(filename)
        setPhoto_gray(final_image)

def cargarImagen_blur():
    global filename, final_image
    if filename:
        final_image = cv2.imread(filename)
        setPhoto_blur(final_image)

def cargarImagen_canny():
    global filename, final_image
    if filename:
        final_image = cv2.imread(filename)
        setPhoto_canny(final_image)

def cargarImagen_mascara():
    global filename, final_image
    if filename:
        final_image = cv2.imread(filename)
        setPhoto_mascara(final_image)

def cargarImagen_degradado():
    global filename, final_image
    if filename:
        final_image = cv2.imread(filename)
        setPhoto_degradado(final_image)

def cargarImagen_ajustar_contraste():
    global filename, final_image
    if filename:
        final_image = cv2.imread(filename)
        setPhoto_ajustar_contraste(final_image)

def cargarImagen_borrosa():
    global filename, final_image
    if filename:
        final_image = cv2.imread(filename)
        setPhoto_borrosa(final_image)


def cargarImagen_recortar():
    global filename, final_image
    if filename:
        final_image = cv2.imread(filename)
        setPhoto_recortar(final_image)

def cargarImagen_detectar_bordes():
    global filename, final_image
    if filename:
        final_image = cv2.imread(filename)
        setPhoto_bordes(final_image)


def salvarImagen():
    global final_image
    if final_image is not None:
        tiempo = time.strftime("%d-%m-%Y-%H-%M-%S")
        cv2.imwrite(f"pollito {tiempo}.jpg", final_image)
        print("Imagen guardada")
    else:
        print("No se puede guardar la imagen porque no se ha procesado ninguna")

def setPhoto(image):
    frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    imagen = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
    imagen = imagen.scaled(400, 280, Qt.KeepAspectRatio)
    window.label.setPixmap(QtGui.QPixmap.fromImage(imagen))

def setPhoto_gray(image):
    global final_image
    final_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    imagen = QImage(final_image, final_image.shape[1], final_image.shape[0], final_image.strides[0], QImage.Format_Grayscale8)
    imagen = imagen.scaled(400, 280, Qt.KeepAspectRatio)
    window.label_2.setPixmap(QtGui.QPixmap.fromImage(imagen))

def setPhoto_blur(image):
    global final_image
    img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    final_image = cv2.GaussianBlur(img, (5, 5), -1)
    imagen = QImage(final_image, final_image.shape[1], final_image.shape[0], final_image.strides[0], QImage.Format_Grayscale8)
    imagen = imagen.scaled(400, 280, Qt.KeepAspectRatio)
    window.label_2.setPixmap(QtGui.QPixmap.fromImage(imagen))

def setPhoto_canny(image):
    global final_image
    img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    final_image = cv2.Canny(img, 200, 200)
    imagen = QImage(final_image, final_image.shape[1], final_image.shape[0], final_image.strides[0], QImage.Format_Grayscale8)
    imagen = imagen.scaled(400, 280, Qt.KeepAspectRatio)
    window.label_2.setPixmap(QtGui.QPixmap.fromImage(imagen))

def setPhoto_mascara(image):
    global final_image
    
    # Convertir la imagen a escala de grises si es necesario
    if len(image.shape) > 2:
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        image_gray = image

    # Crear una matriz de ceros del mismo tamaño que la imagen en escala de grises
    mask = np.zeros_like(image_gray)

    # Definir el centro y el radio del círculo
    cy, cx = mask.shape[0] // 2, mask.shape[1] // 2
    radius = 150

    # Modificar la matriz para contener unos dentro del círculo
    for i in range(mask.shape[0]):
        for j in range(mask.shape[1]):
            if (i - cy) ** 2 + (j - cx) ** 2 < radius ** 2:
                mask[i, j] = 1

    # Aplicar la máscara a la imagen en escala de grises
    result = image_gray * mask

    # Convertir la imagen resultante de nuevo a RGB
    result_rgb = cv2.cvtColor(result.astype(np.uint8), cv2.COLOR_GRAY2RGB)

    # Mostrar el resultado en el widget correspondiente en la interfaz gráfica
    frame = cv2.cvtColor(result_rgb, cv2.COLOR_BGR2RGB)
    height, width, channel = frame.shape
    bytes_per_line = 3 * width
    qImg = QImage(frame.data, width, height, bytes_per_line, QImage.Format_RGB888)
    qImg = qImg.scaled(400, 280, Qt.KeepAspectRatio)
    window.label_2.setPixmap(QtGui.QPixmap.fromImage(qImg))
    

def setPhoto_degradado(image):
    global final_image
    # Convertir la imagen a escala de grises si es necesario
    if len(image.shape) > 2:
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        image_gray = image

    # Crear una matriz de ceros del mismo tamaño que la imagen en escala de grises
    matriz = np.zeros_like(image_gray, dtype=np.float32)

    # Llenar la matriz con un degradado
    for i in range(matriz.shape[0]):
        for j in range(matriz.shape[1]):
            matriz[i, j] = (i + j) / (matriz.shape[0] + matriz.shape[1])

    # Aplicar el degradado a la imagen de escala de grises
    image_degradada = np.multiply(image_gray, matriz)

    # Convertir los valores de la imagen degradada a valores de 8 bits
    image_degradada = np.clip(image_degradada, 0, 255).astype(np.uint8)

    # Visualizar la imagen degradada en el widget correspondiente en la interfaz gráfica
    frame = cv2.cvtColor(image_degradada, cv2.COLOR_GRAY2RGB)
    height, width, channel = frame.shape
    bytes_per_line = 3 * width
    qImg = QImage(frame.data, width, height, bytes_per_line, QImage.Format_RGB888)
    qImg = qImg.scaled(400, 280, Qt.KeepAspectRatio)
    window.label_2.setPixmap(QtGui.QPixmap.fromImage(qImg))

def setPhoto_recortar(image):
    global final_image

    # Convertir la imagen a escala de grises si es necesario
    #if len(image.shape) > 2:
    #    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #else:
    #    image_gray = image

    # Obtener las dimensiones de la imagen
    height, width = image.shape[0:2]

    # Calcular las coordenadas para el recorte
    starRow = int(height * .15)
    starCol = int(width * .15)
    endRow = int(height * .85)
    endCol = int(width * .85)

    # Recortar la región de interés
    croppedImage = image[starRow:endRow, starCol:endCol]

    # Convertir la imagen recortada a formato QImage
    #if len(croppedImage.shape) > 2:
        # Si es una imagen a color, convertir a RGB
    croppedImage = cv2.cvtColor(croppedImage, cv2.COLOR_BGR2RGB)
    #else:
        # Si es una imagen en escala de grises, mantener el formato
    #    croppedImage = cv2.cvtColor(croppedImage, cv2.COLOR_GRAY2RGB)

    # Escalar la imagen para mostrarla en el widget de la interfaz gráfica
    height, width, channel = croppedImage.shape
    bytes_per_line = 3 * width
    qImg = QImage(croppedImage.data, width, height, bytes_per_line, QImage.Format_RGB888)
    qImg = qImg.scaled(400, 280, Qt.KeepAspectRatio)

    # Guardar la imagen recortada
    global filename
    if filename:
        tiempo = time.strftime("%d-%m-%Y-%H-%M-%S")
        cv2.imwrite(f"recorte_{tiempo}.jpg", croppedImage)
        print("Imagen recortada guardada")

    # Mostrar la imagen recortada en el widget correspondiente
    window.label_2.setPixmap(QtGui.QPixmap.fromImage(qImg))

#def setPhoto_bordes():

def setPhoto_bordes(image):
    global final_image
    
    # Convertir la imagen a escala de grises si es necesario
    if len(image.shape) > 2:
        img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        img = image

    # Detectar los bordes utilizando el algoritmo Canny
    edge_img = cv2.Canny(img, 100, 200)

    # Mostrar la imagen con bordes detectados en el widget correspondiente
    frame = cv2.cvtColor(edge_img, cv2.COLOR_GRAY2RGB)
    height, width, channel = frame.shape
    bytes_per_line = 3 * width
    qImg = QImage(frame.data, width, height, bytes_per_line, QImage.Format_RGB888)
    qImg = qImg.scaled(400, 280, Qt.KeepAspectRatio)
    window.label_2.setPixmap(QtGui.QPixmap.fromImage(qImg))

    # Almacenar la imagen final con bordes detectados para futuras operaciones
    final_image = edge_img


def setPhoto_ajustar_contraste(image):
    #def setPhoto_ajustar_contraste(image):
    global final_image

    # Ajustar el contraste de la imagen
    final_image = cv2.addWeighted(image, 2.5, np.zeros(image.shape, image.dtype), 0, 0)
        
    # Convertir la imagen a formato QImage para mostrarla en la interfaz gráfica
    frame = cv2.cvtColor(final_image, cv2.COLOR_BGR2RGB)
    height, width, channel = frame.shape
    bytes_per_line = 3 * width
    qImg = QImage(frame.data, width, height, bytes_per_line, QImage.Format_RGB888)
    qImg = qImg.scaled(400, 280, Qt.KeepAspectRatio)
#*****************************************    
#Este es un ejemplo para quitar el bug de doble guardado
#***********************************************
    #global filename
    #if filename:
    #    tiempo = time.strftime("%d-%m-%Y-%H-%M-%S")
    #    cv2.imwrite(f"ajustar_contraste_{tiempo}.jpg", contrast_img)
    #    print("Imagen con contraste ajustado guardada")
    
    # Mostrar la imagen en el widget correspondiente
    window.label_2.setPixmap(QtGui.QPixmap.fromImage(qImg))
    
    
def setPhoto_borrosa(image):
    #def setPhoto_borrosa(image):
    global final_image
    
    # Aplicar desenfoque gaussiano a la imagen
    blur_image = cv2.GaussianBlur(image, (7, 7), 0)
    final_image = blur_image
        
    # Convertir la imagen a formato QImage para mostrarla en la interfaz gráfica
    frame = cv2.cvtColor(blur_image, cv2.COLOR_BGR2RGB)
    height, width, channel = frame.shape
    bytes_per_line = 3 * width
    qImg = QImage(frame.data, width, height, bytes_per_line, QImage.Format_RGB888)
    qImg = qImg.scaled(400, 280, Qt.KeepAspectRatio)

    # Mostrar la imagen en el widget correspondiente
    window.label_2.setPixmap(QtGui.QPixmap.fromImage(qImg))
  


def salir():
    app.exit()

# Botones
window.cargar_imagen.clicked.connect(cargarImagen)
window.gris.clicked.connect(cargarImagen_gray)
window.blur.clicked.connect(cargarImagen_blur)
window.canny.clicked.connect(cargarImagen_canny)
window.salir.clicked.connect(salir)
window.guardar.clicked.connect(salvarImagen)
window.mascara_imagen.clicked.connect(cargarImagen_mascara)
window.degradado_imagen.clicked.connect(cargarImagen_degradado)
window.recortar_imagen.clicked.connect(cargarImagen_recortar)
window.bordes.clicked.connect(cargarImagen_detectar_bordes)
window.ajustar_contraste.clicked.connect(cargarImagen_ajustar_contraste)
window.borrosa.clicked.connect(cargarImagen_borrosa)
# Ejecutable
window.show()
app.exec()

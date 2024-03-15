 #lena degradada

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargar la imagen de Lena
lena_img = cv2.imread('lenna.png', cv2.IMREAD_GRAYSCALE)

# Crear una matriz de tamaño igual a la imagen de Lena
matriz = np.zeros_like(lena_img, dtype=np.float32)

# Llenar la matriz con un degradado
for i in range(matriz.shape[0]):
    for j in range(matriz.shape[1]):
        matriz[i, j] = (i + j) / (matriz.shape[0] + matriz.shape[1])

# Aplicar el degradado a la imagen de Lena
lena_degradada = np.multiply(lena_img, matriz)

# Convertir los valores de la imagen degradada a valores de 8 bits
lena_degradada = np.clip(lena_degradada, 0, 255).astype(np.uint8)

# Visualizar la imagen original y la imagen degradada
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(lena_img, cmap='gray')
plt.title('Imagen Original')
plt.axis('on')

plt.subplot(1, 2, 2)
plt.imshow(lena_degradada, cmap='gray')
plt.title('Imagen con Degradado')
plt.axis('on')

plt.show()

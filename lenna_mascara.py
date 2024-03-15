 #mascara lena
import cv2
import numpy as np
import matplotlib.pyplot as plt
# Leer la imagen y convertirla a float
image = cv2.imread('lenna.png', cv2.IMREAD_GRAYSCALE).astype(np.float32)

# Crear una matriz de ceros del mismo tamaño que la imagen
mask = np.zeros_like(image)

# Definir el centro y el radio del círculo
cy, cx = mask.shape[0] // 2, mask.shape[1] // 2
radius = 150
# Modificar la matriz para contener unos dentro del círculo
for i in range(mask.shape[0]):
    for j in range(mask.shape[1]):
        if (i - cy) ** 2 + (j - cx) ** 2 < radius ** 2:
            mask[i, j] = 1
# Multiplicar la imagen por la máscara
result = image * mask
# Mostrar el resultado
plt.figure(figsize=(10, 5))
# Imagen original
plt.subplot(1, 3, 1)
plt.imshow(image, cmap='gray')
plt.title('Imagen Original')
# Máscara
plt.subplot(1, 3, 2)
plt.imshow(mask, cmap='gray')
plt.title('Máscara')
# Resultado
plt.subplot(1, 3, 3)
plt.imshow(result, cmap='gray')
plt.title('Resultado')
plt.show()


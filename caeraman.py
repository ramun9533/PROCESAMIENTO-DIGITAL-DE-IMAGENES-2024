 #mascara lena
import cv2
import numpy as np
import matplotlib.pyplot as plt
# Leer la imagen y convertirla a float
image = cv2.imread('cameraman.png', cv2.IMREAD_GRAYSCALE).astype(np.float32)

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


#cameraman

import cv2
import numpy as np
import matplotlib.pyplot as plt

def extract_image_region(image_path, x_range, y_range):
    # Leer la imagen
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE).astype(np.float32)

    # Extraer la región especificada
    extracted_region = image[y_range[0]:y_range[1], x_range[0]:x_range[1]]

    # Crear una figura para mostrar la imagen original y la región extraída
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    axes[0].imshow(image, cmap='gray')
    axes[0].set_title('Imagen Original')
    axes[1].imshow(extracted_region, cmap='gray')
    axes[1].set_title('Región Extraída')
    plt.show()

    return extracted_region

# Ruta de la imagen
image_path = 'cameraman.tif'

# Rango de píxeles para la región de la cabeza del cameraman
x_range = (40, 180)
y_range = (20, 140)

# Extraer la región de la imagen
extracted_region = extract_image_region(image_path, x_range, y_range)


# Prueba de imágenes

import numpy as np
import matplotlib.pyplot as plt


matriz = np.array([[2, 4, 6], [0, 2, 10], [5, 5, 8]])
print(matriz)
print(matriz.shape) #filas y columnas
print(matriz[0, 1]) #Fila 0 Columna 1

plt.imshow(matriz, cmap="viridis")
plt.colorbar()
plt.show()
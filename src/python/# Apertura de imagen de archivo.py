# Apertura de imagen de archivo
import matplotlib.pyplot as plt
from pathlib import Path
ruta = Path(__file__).parent / "foto.jpg"
imagen = plt.imread(ruta)

rojo = imagen[:,:,0]
verde = imagen[:,:,1]
azul = imagen[:,:,2]



plt.figure(1)
plt.imshow(imagen)

plt.figure(2)
plt.imshow(rojo, cmap = "Reds")
plt.colorbar()

plt.figure(3)
plt.imshow(verde, cmap = "Greens")
plt.colorbar()

plt.figure(4)
plt.imshow(azul, cmap = "Blues")
plt.colorbar()

plt.show()
import matplotlib.pyplot as plt
from pathlib import Path
import rasterio
import numpy as np

carpeta = Path(__file__).parent 

with rasterio.open(carpeta / "B04.tif") as src:
    rojo = src.read(1)
with rasterio.open(carpeta / "B03.tif") as src:
    verde = src.read(1)
with rasterio.open(carpeta / "B02.tif") as src:
    azul = src.read(1)
with rasterio.open(carpeta / "B08.tif") as src:
    ir = src.read(1)
with rasterio.open(carpeta / "B12.tif") as src:
    swir = src.read(1)


rgb = np.dstack((rojo, verde, azul))
plt.figure(1)
plt.imshow(rgb)

plt.figure(2)
plt.imshow(rojo)

plt.figure(3)
plt.imshow(verde)

plt.figure(4)
plt.imshow(azul)

plt.figure(5)
plt.imshow(ir, cmap="gray")

plt.figure(6)
plt.imshow(swir, cmap="Reds")

plt.figure(7)
falso_color = np.dstack((ir, rojo, verde))
plt.imshow(falso_color)

ndvi = (ir - rojo) / (ir + rojo)
vegetacion = ndvi > 0.4
print(f"Porcentaje: {vegetacion.mean() * 100:.1f} %")
plt.figure(8)
plt.imshow(ndvi, cmap="RdYlGn", vmin=-1, vmax=1)
plt.colorbar(label="NDVI")

plt.figure(9)
plt.imshow(vegetacion, cmap="gray")

plt.show()

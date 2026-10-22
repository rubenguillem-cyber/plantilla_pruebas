# Imágenes Saler
import matplotlib.pyplot as plt
from pathlib import Path
import rasterio
import numpy as np

carpeta = Path(__file__).parent 

with rasterio.open(carpeta / "20260819/B04_reflectancia_20m.tif") as src:
    rojo_a = src.read(1)
with rasterio.open(carpeta / "20260819/B03_reflectancia_20m.tif") as src:
    verde_a = src.read(1)
with rasterio.open(carpeta / "20260819/B02_reflectancia_20m.tif") as src:
    azul_a = src.read(1)
with rasterio.open(carpeta / "20260819/B08_reflectancia_20m.tif") as src:
    ir_a = src.read(1)
with rasterio.open(carpeta / "20260819/B12_reflectancia_20m.tif") as src:
    swir_a = src.read(1)


rgb_a = np.dstack((rojo_a, verde_a, azul_a))

plt.figure(1)
plt.imshow(rgb_a)

plt.show()
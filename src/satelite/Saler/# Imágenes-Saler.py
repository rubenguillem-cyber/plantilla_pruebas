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

with rasterio.open(carpeta / "20260829/B04_reflectancia_20m.tif") as src:
    rojo_d = src.read(1)
with rasterio.open(carpeta / "20260829/B03_reflectancia_20m.tif") as src:
    verde_d = src.read(1)
with rasterio.open(carpeta / "20260829/B02_reflectancia_20m.tif") as src:
    azul_d = src.read(1)
with rasterio.open(carpeta / "20260829/B08_reflectancia_20m.tif") as src:
    ir_d = src.read(1)
with rasterio.open(carpeta / "20260829/B12_reflectancia_20m.tif") as src:
    swir_d = src.read(1)


rgb_a = np.dstack((rojo_a, verde_a, azul_a))
ndvi_a = (ir_a-rojo_a) / (ir_a + rojo_a)
ndvi_d = (ir_d-rojo_d) / (ir_d + rojo_d)
quem_ndvi = (ndvi_a > 0.4) & (ndvi_d < 0.2)

plt.figure(1)
plt.imshow(rgb_a)

plt.figure(2)
plt.imshow(ndvi_d, cmap="RdYlGn", vmin=-1, vmax=1)

plt.figure(3)
plt.imshow(quem_ndvi)

plt.show()
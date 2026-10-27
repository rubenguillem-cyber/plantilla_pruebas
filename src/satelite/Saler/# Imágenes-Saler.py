# Imágenes Saler
import matplotlib.pyplot as plt
from pathlib import Path
import rasterio
import numpy as np
from matplotlib.colors import ListedColormap
from matplotlib.patches import Patch

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
nbr_a = (ir_a - swir_a) / (ir_a + swir_a)
nbr_d = (ir_d - swir_d) / (ir_d + swir_d)
nbr_dif = nbr_a - nbr_d
quem_nbr = (nbr_dif > 0.2) & (ndvi_a > 0.4)
area_ndvi = np.count_nonzero(quem_ndvi) * 20 * 20 / 10000
area_nbr = np.count_nonzero(quem_nbr) * 20 * 20 / 10000
severidad = np.zeros(nbr_dif.shape, dtype=int)

vegetacion = ndvi_a > 0.4

severidad[(nbr_dif >= 0.1) & (nbr_dif < 0.27) & vegetacion] = 1
severidad[(nbr_dif >= 0.27) & (nbr_dif < 0.66) & vegetacion] = 2
severidad[(nbr_dif >= 0.66) & vegetacion] = 3
print(f"El area calculada con ndvi es {area_ndvi} ha")
print(f"El area calculada con nbr es {area_nbr} ha")

plt.figure(1)
plt.imshow(rgb_a)

plt.figure(2)
plt.imshow(ndvi_d, cmap="RdYlGn", vmin=-1, vmax=1)

plt.figure(3)
plt.imshow(quem_ndvi)

plt.figure(4)
plt.imshow(quem_nbr)

colores = ListedColormap(["yellow", "orange", "red"])

plt.figure(5)
plt.imshow(rgb_a)

plt.imshow(
    np.ma.masked_equal(severidad, 0),
    cmap=colores,
    vmin=0.5,
    vmax=3.5,
    alpha=0.85
)

plt.legend(handles=[
    Patch(color="yellow", label="Baja"),
    Patch(color="orange", label="Media"),
    Patch(color="red", label="Alta")
])

plt.title("Severidad estimada del incendio")

plt.show()
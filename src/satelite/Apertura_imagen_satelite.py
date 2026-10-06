import matplotlib.pyplot as plt
from pathlib import Path
ruta = Path(__file__).parent / "foto.jpg"
imagen = plt.imread(ruta)
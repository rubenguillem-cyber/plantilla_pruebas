# Plantilla de cuaderno técnico — Informática II

Esta es la plantilla maestra del proyecto docente `Informatica-II`. No es un
repositorio de alumnado y no contiene una carpeta `.git`.

## Uso local ordinario

1. Descarga el ZIP de Classroom y descomprímelo.
2. Coloca su única carpeta `informatica-2bach/` en
   `~/Documentos/Informatica-II/`.
3. Abre la carpeta completa en VS Code.
4. Inicializa el historial con `git init` y configura la identidad solo en este
   repositorio mediante `git config --local`.
5. Edita, ejecuta o revisa, guarda y crea commits locales.

No necesitas iniciar sesión, conexión, GitHub ni GitHub Pages para trabajar.
Un commit guarda una versión local. La sincronización con GitHub es ocasional,
se realiza únicamente cuando lo indica el profesor y se documenta por separado.

`docs/` contiene las páginas de la web local; `src/` guarda el código fuente.
MkDocs permite revisar la web local desde la raíz del proyecto con:

```bash
~/informatica2-env/bin/python -m mkdocs serve
```

Sustituye los recordatorios por evidencias propias y no incluyas datos
personales, credenciales ni resultados sin comprobar.

La carpeta `.github/workflows/pages.yml` se conserva para una publicación
posterior autorizada; no afecta al trabajo local.

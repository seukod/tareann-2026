# tareann-2026

Proyecto de ejemplo para tareas de IA.

## Entorno Conda

Para crear el entorno recomendado para esta tarea:

```bash
conda env create -f environment.yml
conda activate tarea1
```

Para actualizar el entorno desde `environment.yml`:

```bash
conda env update -f environment.yml --prune
```

Si usas VS Code y el notebook necesita el kernel, ejecuta:

```bash
python -m ipykernel install --user --name=tarea1 --display-name "Python (tarea1)"
```

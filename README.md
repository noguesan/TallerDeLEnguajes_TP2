# Proyecto: Simulación de Rondas y Análisis de Resultados

Este proyecto corresponde al ejercicio 10 de la practiva subida 
simula el desarrollo de varias rondas de juego a partir de un archivo JSON de entrada, permitiendo analizar los resultados y extraer conclusiones, como la performance de los participantes.

El código fuente con las funciones necesarias se encuentra en el directorio `src`, mientras que los datos de entrada están en la carpeta `data`.

## Instalación de Dependencias

Este proyecto no requiere librerías externas, solo se utiliza la biblioteca estándar de Python.  
Sin embargo, se recomienda crear un entorno virtual para aislar el entorno de desarrollo.

### 1. Crear un entorno virtual (opcional pero recomendado)
```bash
python -m venv venv
```

### 2. Activar el entorno virtual
- En Windows:
  ```bash
  venv\Scripts\activate
  ```
- En macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

## Ejecución del Proyecto

Para ejecutar la simulación de las rondas, corré el script principal desde la raíz del proyecto:

```bash
python main.py
```

Asegurate de que el archivo `rondas.json` esté disponible en la carpeta `data/`.

## Estructura del Proyecto
```
proyecto/
│── enunciado/             # Carpeta con los archivos del enunciado de la practica
│   ├── 02-practica.pdf    # Enunciado de la practica 
│   ├── 02-practica.ipynb  # Resolucion de practica entera
│
│── data/                  # Carpeta con archivos de datos
│   ├── rondas.json        # Datos con la configuración de las rondas
│
│── src/                   # Código fuente
│   ├── funciones.py       # Funciones utilizadas por main.py
│   ├── __init__.py        # Convierte a 'src' en un paquete
│
│── main.py                # Script principal que ejecuta la simulación
│── requirements.txt       # (Opcional) Archivo con dependencias
│── README.md              # Documentación del proyecto
```

## Notas

- El módulo `json` utilizado forma parte de la biblioteca estándar de Python.
- No se requieren instalaciones adicionales para correr este proyecto.
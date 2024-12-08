# Proyecto de Cálculo de Incertidumbres en Medición

Este repositorio contiene scripts en Python asociados al taller #2 Física experimental. 
Este consiste en el entendimiento de la relación potencial y como desarrollarla, la generación de gráficas en la relación t vs d y t vs h en escala milimétrica y escala logarítmica..

## Contenido del Proyecto

### Archivos Principales

- **`graficas.py`**:
  - Permite ver las gráficas en la relación t vs d y y vs h en escala milimétrica y escala log - log.

- **`exponentes_negativos.py`**


- **`estimacion_tiempos.py`**:
  - Código para predecir nuevos tiempos, cambiando el valor de las variables d y h.

- **`formula_general.py`**:
  - Calculo para comparar los tiempos experimentales con los tiempos resultantes de la formula general planteada en el taller.


- **`Tener en cuenta`**:
  - En caso de implementarlo recuerda tener instalado python en tu computadora, e instalar las librería numpy especializada en el cálculo numérico y analisis de datos, matplotlib para la generación de las gráficas y pandas para el manejo y análisis de estructura de datos. Además de entender la función scipy.optimize para ajuste de curvas y regresiones lineales.

-**`Contacto`**:
  - jrodriguezvar@unal.edu.co

## Requisitos e instalación

- **Python 3.6 o superior**.
- **Biblioteca NumPy, matplotlib y pandas.**
  ```bash
  pip3 install numpy matplotlib pandas

- **Ejecutar (ejemplo).**

```bash
  python3 formula_general.py

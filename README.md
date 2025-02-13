# LAB2-Convolución, correlación y transformación 
## INTRODUCCION 
En el análisis de señales y sistemas, sirven para comprender la interacción entre señales y los sistemas que las procesan son fundamentales para múltiples aplicaciones en ingeniería. Se encuentran tres operaciones matemáticas que juegan un papel clave en este estudio: la convolución, la correlación y las transformadas.
La convolución permite determinar cómo un sistema responde a una señal de entrada, siendo esencial en el análisis de sistemas lineales e invariantes en el tiempo (LTI). La correlación, por su parte, mide la similitud entre dos señales a lo largo del tiempo, siendo una herramienta valiosa en el procesamiento de señales, la detección de patrones y la reducción de ruido. Las transformadas por su parte, como la de Fourier y la de Laplace, facilitan el análisis de señales en el dominio de la frecuencia. Estas herramientas permiten descomponer señales en sus componentes fundamentales, optimizando tareas como el diseño de filtros y la compresión de datos.
## PROCEDIMIENTO 
Se realizó un estudio con tres estudiantes, donde se estableció un sistema y una señal de entrada basados en sus datos personales. Para cada estudiante:

Se definió el sistema h[n] como una secuencia discreta formada por los dígitos de su código de estudiante.
Se definió la señal de entrada x[n] como la secuencia compuesta por los dígitos de su número de cédula.
A partir de estas secuencias, se obtuvo la señal de salida y[n] mediante la operación de convolución discreta.
El cálculo de la convolución se realizó en dos etapas:
- Cálculo manual con sumatorias, aplicando la definición de convolución discreta para encontrar y[n].
- Implementación en Python, utilizando funciones numéricas para verificar los resultados obtenidos manualmente y agilizar el cálculo para cada conjunto de datos.
  
  ```pitón
   #Definir señales x(n) e h(n) para tres casos
    x1 = np.array([1, 0, 1, 4, 7, 3, 7, 8, 8, 6])
    h1 = np.array([5, 6, 0, 0, 6, 0, 7])

    x2 = np.array([1, 1, 0, 0, 9, 4, 8, 8, 6, 6])
    h2 = np.array([5, 6, 0, 0, 6, 1, 4])

    x3 = np.array([1, 0, 0, 1, 0, 6, 7, 1, 1, 8])
    h3 = np.array([5, 6, 0, 0, 7, 0, 8])

    # Calcular convoluciones
    y1 = np.convolve(x1, h1, mode='full')
    y2 = np.convolve(x2, h2, mode='full')
    y3 = np.convolve(x3, h3, mode='full')

    # Crear los ejes de tiempo
    n_y1 = np.arange(len(y1))
    n_y2 = np.arange(len(y2))
    n_y3 = np.arange(len(y3))

```

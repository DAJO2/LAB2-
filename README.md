# LAB2-Convolución, correlación y transformación 
## INTRODUCCION 
En el análisis de señales y sistemas, sirven para comprender la interacción entre señales y los sistemas que las procesan son fundamentales para múltiples aplicaciones en ingeniería. Se encuentran tres operaciones matemáticas que juegan un papel clave en este estudio: la convolución, la correlación y las transformadas.
La convolución permite determinar cómo un sistema responde a una señal de entrada, siendo esencial en el análisis de sistemas lineales e invariantes en el tiempo (LTI). La correlación, por su parte, mide la similitud entre dos señales a lo largo del tiempo, siendo una herramienta valiosa en el procesamiento de señales, la detección de patrones y la reducción de ruido. Las transformadas por su parte, como la de Fourier, facilitan el análisis de señales en el dominio de la frecuencia. Estas herramientas permiten descomponer señales en sus componentes fundamentales, optimizando la compresión de datos.
## PROCEDIMIENTO 
### CONVOLUCIÓN
Se realizó un estudio con tres estudiantes, donde se estableció un sistema y una señal de entrada basados en sus datos personales. Para cada estudiante:

Se definió el sistema h[n] como una secuencia discreta formada por los dígitos de su código de estudiante.
Se definió la señal de entrada x[n] como la secuencia compuesta por los dígitos de su número de identidad.
A partir de estas secuencias, se obtuvo la señal de salida y[n] mediante la operación de convolución discreta.
El cálculo de la convolución se realizó en dos etapas:
- Cálculo manual con sumatorias , aplicando la definición de convolución discreta para encontrar y[n].
- Implementación en Python, utilizando funciones numéricas para verificar los resultados obtenidos manualmente y se agiliza el cálculo para cada conjunto de datos realizando la convolución discreta entre señales de entrada.

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
- Se muestran los tres tipos de convolucion:

  
![](https://github.com/DAJO2/LAB2-/blob/main/DIEGOJIMENEZCONVOLUCION.png)
![](https://github.com/DAJO2/LAB2-/blob/main/GABRIELANARANJOCONVOLUCION.png)
![](https://github.com/DAJO2/LAB2-/blob/main/CARLOSBERNALCONVOLUCION.png)

### CORRELACIÓN
Para encontrar la correlación entre las señales, se definieron dos señales de tiempo discreto, muestreadas con un período de muestreo 
Ts =1.25 ms:
  ``` pitón
  fs = 1 / 1.25e-3
  n = np.arange(9)
  ts = 1.25e-3

  x1 = np.cos(2 * np.pi * 100 * n * ts)
  x2 = np.sin(2 * np.pi * 100 * n * ts)

  y = np.correlate(x1, x2, mode='full')

  r = np.corrcoef(x1, x2)[0, 1]
```
- Se observa que ambas señales son funciones armónicas con una frecuencia de 100 Hz y están desfasadas 90° entre sí (una es un coseno y la otra un seno):
![](https://github.com/DAJO2/LAB2-/blob/main/SEÑALES_SIN_COS.png)
El Coeficiente de correlación de Pearson: -0.00000000000000002675899923417194801263392048393010
Este número es prácticamente cero, lo que indica que las señales x1[n] (coseno) y x2[n] (seno) son no correlacionadas en promedio.
 ¿Por qué es casi cero?
La correlación entre un coseno y un seno de la misma frecuencia es cero, ya que están desfasados 90°. Esto indica que, en el dominio del tiempo, las señales son ortogonales y no presentan una relación lineal directa.
### TRANSFORMADA
Por medio de la pagina de physionet se descargo una señal tipo EEG en reposo con ojos cerrados debido a que con los ojos cerrados, el cerebro genera predominantemente ondas alfa en la región occipital y parietal, estas ondas son clave en estudios de neurofisiología y sirven como referencia para identificar patrones normales de actividad cerebral. Ademas a esto se reduce la influencia de estímulos visuales en la actividad cerebral, permitiendo un análisis más limpio de la señal EEG sin artefactos inducidos por el parpadeo o el procesamiento visual. Donde la señal fue grabada con una tasa de 160 muestras por segundo.
![](https://github.com/DAJO2/LAB2-/blob/main/SENALFT.png)

Para analizar la señal EEG en reposo con ojos cerrados, es fundamental calcular sus características en el dominio del tiempo. Esto incluye estadísticos descriptivos y frecuencia de muestreo, los que se calcularon por medio de estas funciones:
 ``` pitón
num_signals = edf.signals_in_file
fs = edf.getSampleFrequency(0)
signal_labels = edf.getSignalLabels()

signal = edf.readSignal(0)
edf.close()

time = np.arange(len(signal)) / fs

data_mean = np.mean(signal)
data_std = np.std(signal, ddof=1)
data_var = np.var(signal, ddof=1)
data_median = np.median(signal)
```
Se aplica la Transformada de Fourier (TF) ya que permite analizar la señal EEG en el dominio de la frecuencia, descomponiéndola en sus componentes espectrales (Power Spectral Density, PSD) que indica cómo se distribuye la energía de la señal en el espectro de frecuencias.
 ``` pitón
N = len(signal)
freqs = np.fft.fftfreq(N, d=1/fs)
spectrum = np.abs(fft(signal))
f_welch, psd = welch(signal, fs, nperseg=1024)
```
- Transformada de Furier de la señal EEG
![](https://github.com/DAJO2/LAB2-/blob/main/TRANSFORMADADEFOURIER.png)

- Densidad espectral de potencia(PSD)
![](https://github.com/DAJO2/LAB2-/blob/main/DENSIDADESPECTRAL.png)

Se analizaron los estadísticos descriptivos en función de la frecuencia para caracterizar la señal EEG en el dominio espectral. Se calcularon la frecuencia media y la frecuencia mediana para identificar la tendencia central de la distribución de frecuencias, junto con la desviación estándar, que mide la dispersión de la señal respecto a su frecuencia promedio. Además, se generó un histograma de frecuencias, permitiendo visualizar la distribución de la energía en diferentes rangos del espectro en estado de reposo con ojos cerrados.
``` pitón
freq_mean = np.sum(f_welch * psd) / np.sum(psd)
freq_median = f_welch[np.cumsum(psd) >= np.sum(psd) / 2][0]
freq_std = np.sqrt(np.sum(psd * (f_welch - freq_mean) ** 2) / np.sum(psd))
```
- Histograma señal EEG
![](https://github.com/DAJO2/LAB2-/blob/main/HISTOGRAMA.png)

- Resultados de los estadisticos descriptivos

![](https://github.com/DAJO2/LAB2-/blob/main/Captura.png)
#### Requirements:
- python 3.9
- matplotlib
- pyedflib

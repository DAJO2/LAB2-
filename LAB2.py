import numpy as np
import matplotlib.pyplot as plt
import pyedflib
from scipy.fftpack import fft
from scipy.signal import welch

# Definir señales x(n) e h(n) para tres casos
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

plt.figure(figsize=(8, 4))
plt.stem(n_y1, y1, basefmt="black", linefmt="C2-", markerfmt="C2o")
plt.title("Convolucion 1. Diego Jimenez.")
plt.xlabel("n")
plt.ylabel("Amplitud")
plt.grid()
plt.show()

plt.figure(figsize=(8, 4))
plt.stem(n_y2, y2, basefmt="black", linefmt="C3-", markerfmt="C3o")
plt.title("Convolucion 2. Gabriela Naranjo.")
plt.xlabel("n")
plt.ylabel("Amplitud")
plt.grid()
plt.show()

plt.figure(figsize=(8, 4))
plt.stem(n_y3, y3, basefmt="black", linefmt="C4-", markerfmt="C4o")
plt.title("Convolucion 3. Carlos Bernal.")
plt.xlabel("n")
plt.ylabel("Amplitud")
plt.grid()
plt.show()

fs = 1 / 1.25e-3
n = np.arange(9)
ts = 1.25e-3

x1 = np.cos(2 * np.pi * 100 * n * ts)
x2 = np.sin(2 * np.pi * 100 * n * ts)

y = np.correlate(x1, x2, mode='full')

r = np.corrcoef(x1, x2)[0, 1]
print(f'Coeficiente de correlación de Pearson: {r:.50f}')

plt.figure(figsize=(10, 4))
plt.subplot(3, 1, 1)
plt.plot(n, x1, marker='o', linestyle='-')
plt.xlabel('n')
plt.ylabel('x1[n]')
plt.title('Señal x1[n] = cos(2π100nTs)')
plt.grid()

plt.subplot(3, 1, 2)
plt.plot(n, x2, marker='o', linestyle='-')
plt.xlabel('n')
plt.ylabel('x2[n]')
plt.title('Señal x2[n] = sin(2π100nTs)')
plt.grid()

lags = np.arange(-len(x1) + 1, len(x1))
plt.subplot(3, 1, 3)
plt.plot(lags, y, marker='o', linestyle='-')
plt.xlabel('Desplazamiento')
plt.ylabel('Correlación')
plt.title('Correlación cruzada entre x1[n] y x2[n]')
plt.grid()

plt.tight_layout()
plt.show()

filename = "C:/Users/ASUS/Documents/UNIVERSIDAD MILITAR NUEVA GRANADA/SEPTIMO SEMESTRE/PROCESAMIENTO DE SEÑALES/LABORATORIO 2/S001R01.edf"

edf = pyedflib.EdfReader(filename)
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

print("=== Estadísticos Descriptivos ===")
print(f"Frecuencia de muestreo: {fs} Hz")
print(f"Media: {data_mean:.5f}")
print(f"Desviación estándar: {data_std:.5f}")
print(f"Varianza: {data_var:.5f}")
print(f"Mediana: {data_median:.5f}")

plt.figure(figsize=(10, 4))
plt.plot(time, signal, label="Señal")
plt.xlabel("Tiempo [s]")
plt.ylabel("Voltaje [V]")
plt.title("Señal en función del tiempo")
plt.legend()
plt.grid()
plt.show()

N = len(signal)
freqs = np.fft.fftfreq(N, d=1/fs)
spectrum = np.abs(fft(signal))

plt.figure(figsize=(10, 4))
plt.plot(freqs[:N // 2], spectrum[:N // 2], label="Espectro de Frecuencia")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Magnitud")
plt.title("Transformada de Fourier de la Señal")
plt.legend()
plt.grid()
plt.show()

f_welch, psd = welch(signal, fs, nperseg=1024)

plt.figure(figsize=(10, 4))
plt.semilogy(f_welch, psd, label="Densidad espectral de potencia")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("PSD [V²/Hz]")
plt.title("Densidad Espectral de Potencia (PSD)")
plt.legend()
plt.grid()
plt.show()

freq_mean = np.sum(f_welch * psd) / np.sum(psd)
freq_median = f_welch[np.cumsum(psd) >= np.sum(psd) / 2][0]
freq_std = np.sqrt(np.sum(psd * (f_welch - freq_mean) ** 2) / np.sum(psd))

plt.figure(figsize=(10, 4))
plt.hist(f_welch, bins=30, color='b', alpha=0.7, edgecolor='black', density=True, label="Histograma de Frecuencias")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Densidad")
plt.title("Histograma de Frecuencias")
plt.legend()
plt.grid()
plt.show()

print(f"Frecuencia Media: {freq_mean:.5f} Hz")
print(f"Frecuencia Mediana: {freq_median:.5f} Hz")
print(f"Desviación Estándar de la Frecuencia: {freq_std:.5f} Hz")


import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile


def my_dtft(x, fs, f):
    """
    Вычисляет значение дискретного во времени преобразования Фурье (ДВПФ) для сигнала x и частоты f.
    
    Параметры:
        x (np.array): Входной сигнал.
        fs (float): Частота дискретизации (в герцах).
        f (float или np.array): Частота (в герцах) или массив частот.
    
    Возвращает:
        float или np.array: Амплитудное значение спектра для заданной частоты или массива частот.
    """
    N = len(x)
    n = np.arange(N)  # Вектор индексов [0, 1, ..., N-1]
    
    if isinstance(f, (int, float)):  # Если f — скаляр
        w = 2 * np.pi * f / fs
        X = np.dot(x, np.exp(-1j * w * n))
        return np.abs(X)
    else:  # Если f — массив частот
        w = 2 * np.pi * f[:, np.newaxis] / fs
        X = np.dot(np.exp(-1j * w * n), x)
        return np.abs(X)
    
fs, x = wavfile.read('record.wav')

if len(x.shape) > 1:
    x = np.mean(x, axis=1)

x = x.astype(np.float32) / np.max(np.abs(x))

frequencies = np.arange(40, 501, 1)

# Вычисление амплитудного спектра с помощью my_dtft
spectrum = my_dtft(x, fs, frequencies)

plt.figure(figsize=(10, 6))
plt.plot(frequencies, spectrum, label='Амплитудный спектр')
plt.title('Амплитудный спектр сигнала')
plt.xlabel('Частота (Гц)')
plt.ylabel('Амплитуда')
plt.grid(True)
plt.legend()

fundamental_frequency = frequencies[np.argmax(spectrum)]
print(f"Частота основного тона (ДВПФ): {fundamental_frequency:.2f} Гц")

plt.show()
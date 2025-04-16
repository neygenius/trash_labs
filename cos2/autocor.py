import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from statsmodels.tsa.stattools import acf
from scipy.signal import find_peaks


# Загрузка аудиофайла
fs, x = wavfile.read('record.wav')  # Загрузка файла

print(fs)
# Если сигнал стерео, преобразуем его в моно
if len(x.shape) > 1:
    x = np.mean(x, axis=1)

# Нормировка сигнала
x = x.astype(np.float32) / np.max(np.abs(x))

# Функция для вычисления АКФ
def my_acf(x, m):
    """
    Вычисляет значение автокорреляционной функции (АКФ) для сигнала x и задержки m.
    
    Параметры:
        x (np.array): Входной сигнал.
        m (int): Задержка (lag).
    
    Возвращает:
        float: Значение АКФ для заданной задержки m.
    """
    N = len(x)
    if m >= N:
        return 0  # Если задержка больше длины сигнала, возвращаем 0
    
    mu = np.mean(x)
    numerator = np.sum((x[:N - m] - mu) * (x[m:] - mu))
    denominator = np.sum((x - mu) ** 2)
    #denominator = N- m
    if denominator == 0:
        return 0
    return numerator / denominator

m_values = range(0, 100)  # Задержки для проверки
my_acf_values = [my_acf(x, m) for m in m_values]

acf_values = acf(x, nlags=len(m_values) - 1, adjusted=True)

print("Сравнение результатов my_acf и библиотечной функции:")
for m, my_val, lib_val in zip(m_values, my_acf_values, acf_values):
    print(f"m = {m}: my_acf = {my_val:.6f}, lib_acf = {lib_val:.6f}")

plt.figure(figsize=(12, 6))
plt.plot(m_values, my_acf_values, label='my_acf', marker='o', linestyle='-', color='blue')
plt.plot(m_values, acf_values, label='statsmodels.acf', marker='x', linestyle='--', color='red')
plt.title('Сравнение my_acf и библиотечной функции АКФ')
plt.xlabel('Задержка (m)')
plt.ylabel('Значение АКФ')
plt.grid(True)
plt.legend()
plt.show()

acf_values = acf(x, nlags=2000, adjusted=True)

# Построение графика АКФ
plt.figure(figsize=(10, 6))
plt.plot(acf_values, label='АКФ')
plt.title('Автокорреляционная функция (АКФ)')
plt.xlabel('Задержка (m)')
plt.ylabel('Значение АКФ')
plt.grid(True)
plt.legend()

peaks, _ = find_peaks(acf_values[20:], height=0.1, distance=10)
if len(peaks) > 0:
    m_max = peaks[0] + 20
    plt.scatter(m_max, acf_values[m_max], color='red', label=f"Пик (m={m_max})")  # метка пика
    f_acf = 1 / (m_max / fs)
    print(f"Оценка основного тона по АКФ: {f_acf:.2f} Гц")
else:
    print("Пики не найдены!")

plt.show()

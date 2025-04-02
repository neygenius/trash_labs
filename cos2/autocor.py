import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from statsmodels.tsa.stattools import acf


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

nlags = len(x) // 2
acf_values = acf(x, nlags=nlags, adjusted=True)

# Построение графика АКФ
plt.figure(figsize=(10, 6))
plt.plot(acf_values, label='АКФ')
plt.title('Автокорреляционная функция (АКФ)')
plt.xlabel('Задержка (m)')
plt.ylabel('Значение АКФ')
plt.grid(True)
plt.legend()

#Первый пик АКФ после m = 0
peaks = np.where((acf_values[1:-1] > acf_values[:-2]) & (acf_values[1:-1] > acf_values[2:]))[0] + 1
first_peak = peaks[0] if len(peaks) > 0 else None

if first_peak is not None:
    # Оценка частоты основного тона
    f0 = fs / first_peak
    print(f"Частота основного тона: {f0:.2f} Гц")
else:
    print("Пики не найдены. Основной тон не обнаружен.")

plt.show()
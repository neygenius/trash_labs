import matplotlib.pyplot as plt
import numpy as np
import pyreaper
import scipy.io.wavfile as wavfile


fs, x = wavfile.read('record.wav')

if len(x.shape) > 1:
    x = np.mean(x, axis=1)

x = x.astype(np.float32) / max(abs(min(x)), abs(max(x)))

# Временная шкала
t = np.linspace(0, (len(x) - 1) / fs, len(x))

# Подготовка данных для REAPER
int16_info = np.iinfo(np.int16)
x = x * min(int16_info.min, int16_info.max)
x = x.astype(np.int16)

pm_times, pm, f_times, f, _ = pyreaper.reaper(x, fs)

plt.figure('[Reaper] Pitch Marks')
plt.plot(t, x, label='Сигнал')
plt.scatter(pm_times[pm == 1], x[(pm_times * fs).astype(int)][pm == 1], marker='x', color='red', label='Pitch Marks')
plt.title('Pitch Marks')
plt.xlabel('Время (с)')
plt.ylabel('Амплитуда')
plt.grid(True)
plt.legend()

plt.figure('[Reaper] Основная частота')
plt.plot(f_times, f, label='Основная частота')
plt.title('Основная частота (F0)')
plt.xlabel('Время (с)')
plt.ylabel('Частота (Гц)')
plt.grid(True)
plt.legend()

average_f0 = np.mean(f[f != -1])
print(f"Средняя частота основного тона: {average_f0:.2f} Гц")

plt.show()
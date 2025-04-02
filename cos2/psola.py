import numpy as np
import pyreaper
import scipy.io.wavfile as wavfile
from scipy.signal import windows


def psola(x, fs, k):
    """
    Изменяет частоту основного тона речи с помощью алгоритма PSOLA.
    
    Параметры:
        x (np.array): Входной сигнал.
        fs (float): Частота дискретизации (в герцах).
        k (float): Коэффициент изменения частоты основного тона.
    
    Возвращает:
        np.array: Сигнал с изменённой частотой основного тона.
    """
    x = x.astype(np.float32) / np.max(np.abs(x))

    # Подготовка данных для REAPER
    int16_info = np.iinfo(np.int16)
    x_reaper = x * min(int16_info.min, int16_info.max)
    x_reaper = x_reaper.astype(np.int16)

    pm_times, pm, f_times, f, _ = pyreaper.reaper(x_reaper, fs)

    segment_centers = pm_times[pm == 1]
    segment_centers = (segment_centers * fs).astype(int)

    T = (fs / np.mean(f[f != -1])).astype(int)

    segment_length = 2 * T

    window = windows.triang(segment_length)

    y = np.zeros(int(len(x) * k))
    output_index = 0

    for center in segment_centers:
        start = max(0, center - T)
        end = min(len(x), center + T)

        segment = x[start:end]

        if len(segment) == segment_length:
            segment *= window

        y[output_index:output_index + len(segment)] += segment
        output_index += int(k * T)

    y = y / np.max(np.abs(y))
    return y


fs, x = wavfile.read('record.wav')

# Если стерео - берём один канал
if len(x.shape) > 1:
    x = x[:, 0]

# Изменение тона (k > 1: выше, k < 1: ниже)
k = 1.5  # Пример: повышаем тон на 50%
y = psola(x, fs, k)

wavfile.write('output_psola.wav', fs, np.float32(y))

print("Результат сохранён в файл output_psola.wav")
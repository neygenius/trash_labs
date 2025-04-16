import numpy as np
import pyreaper
import scipy.io.wavfile as wavfile
from scipy.signal.windows import triang


def psola(x, fs, f_times, f0, k):
    voiced_indices = f0 != -1
    voiced_times = f_times[voiced_indices]
    voiced_f0 = f0[voiced_indices]
    if len(voiced_times) == 0:
        print("Тоновые участки не найдены!")
        return x
    output = np.zeros(len(x))
    window = triang(int(fs / np.mean(voiced_f0) * 2))

    for i, t_center in enumerate(voiced_times):
        T = fs / voiced_f0[i]
        center_idx = int(t_center * fs)
        half_len = len(window) // 2
        start_idx = max(0, center_idx - half_len)
        end_idx = min(len(x), center_idx + half_len)
        chunk = np.zeros(len(window))
        chunk_len = end_idx - start_idx
        chunk[:chunk_len] = x[start_idx:end_idx]
        chunk *= window
        new_center = int(t_center * fs / k)
        new_start = max(0, new_center - half_len)
        new_end = min(len(output), new_center + half_len)
        output[new_start:new_end] += chunk[:new_end - new_start]

    return output / np.max(np.abs(output))


fs, x = wavfile.read('record.wav')

# Если стерео - берём один канал
if len(x.shape) > 1:
    x = x[:, 0]

x = x.astype(np.float32) / np.max(np.abs(x))

int16_info = np.iinfo(np.int16)
x_int16 = np.clip(x * 32767, int16_info.min, int16_info.max).astype(np.int16)
pm_times, pm, f_times, f0, _ = pyreaper.reaper(x_int16, fs)

# Изменение тона (k > 1: выше, k < 1: ниже)
k = 1.2  # Пример: повышаем тон на 20%
x_psola = psola(x, fs, f_times, f0, k)

wavfile.write('output.wav', fs, (x_psola * 32767).astype(np.int16))

print("Результат сохранён в файл output.wav")

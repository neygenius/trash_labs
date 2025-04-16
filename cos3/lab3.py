import numpy as np
import scipy.io.wavfile as wavfile
from math import sin, pi
from multiprocessing import Pool


def linear_interpolation(a, b, n1, n2, n):
    return a + (b - a) * (n - n1) / (n2 - n1)


def shift(x, fs, delta_0, A_delta, f_delta):
    N = len(x)
    t1 = np.zeros(N)

    for i in range(0, N):
        # исходное время для i-ого отсчета + постоянный сдвиг + синусоидальное изменение сдвига
        t1[i] = i/fs + delta_0 + A_delta * sin(2*pi*f_delta * i)

    if not np.all(np.diff(t1) > 0): print(f"Метки не возрастают, плохо подобраны параметры")
    return t1


def interpolation_new_signal(t_shift, x, fs):
    t = np.zeros_like(x)
    res = np.zeros_like(x)
    prev_j = 0

    for i in range(0, len(x)):
        t[i] = i / fs

    for i in range(0, len(t)):
        for j in range(prev_j, len(t_shift)):
            if t[i] > t_shift[j] and t[i] < t_shift[j + 1]:
                prev_j = j
                res[i] = linear_interpolation(x[j], x[j + 1], t_shift[j], t_shift[j + 1], t[i])
                break
    return res


if __name__ == '__main__':

    fs, x = wavfile.read("record.wav")

    # Если стерео - берём один канал
    if len(x.shape) > 1:
        x = x[:, 0]

    x = x.astype(np.float32) / np.max(np.abs(x))

    # Вычисление временных меток
    t1 = shift(x, fs, 0.02, 0.01, 3)
    t2 = shift(x, fs, 0.025, 0.005, 3)
    t3 = shift(x, fs, 0.030, 0.015, 4)
    t4 = shift(x, fs, 0.035, 0.020, 4)

    with Pool(20) as p:
        x1 = p.apply(interpolation_new_signal, [t1, x, fs])
        x2 = p.apply(interpolation_new_signal, [t2, x, fs])
        x3 = p.apply(interpolation_new_signal, [t3, x, fs])
        x4 = p.apply(interpolation_new_signal, [t4, x, fs])

    # Хорус эффект 
    res = x + x1+ x2 + x3 + x4 
    res /= res.max()
    wavfile.write("result.wav", fs, np.float32(res))
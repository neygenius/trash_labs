# pylint: disable=invalid-name,missing-docstring,too-few-public-methods

import unittest

import numpy as np
from scipy.fft import fft
from scipy.signal import stft

import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from scipy.io import wavfile


def dft(x: np.ndarray) -> np.ndarray:
    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(-2j * np.pi * k * n / N)
    return np.dot(M, x)


def real_stft(x: np.ndarray, segment: int, overlap: int) -> np.ndarray:
    n = x.shape[0]
    assert len(x.shape) == 1
    assert segment < n
    assert overlap < segment

    hop_size = segment - overlap
    num_segments = 1 + (n - segment) // hop_size
    
    stft_matrix = []
    
    # Прямоугольное окно (boxcar) - просто берем сегмент без дополнительного взвешивани
    for i in range(num_segments):
        start = i * hop_size
        end = start + segment
        segment_data = x[start:end]
        spectrum = dft(segment_data)
        # Берём только положительные частоты (как scipy.signal.stft)
        stft_matrix.append(spectrum[: segment // 2 + 1])
    
    return np.array(stft_matrix).T


class Test(unittest.TestCase):
    class Params:
        def __init__(self, n: int, segment: int, overlap: int) -> None:
            self.n = n
            self.segment = segment
            self.overlap = overlap

        def __str__(self) -> str:
            return f"n={self.n} segment={self.segment} overlap={self.overlap}"
    
    def test_dft(self) -> None:
        for n in (10, 11, 12, 13, 14, 15, 16):
            with self.subTest(n=n):
                np.random.seed(0)
                x = np.random.rand(n) + 1j * np.random.rand(n)
                actual = dft(x)
                expected = fft(x)
                self.assertTrue(np.allclose(actual, expected))

    def test_stft(self) -> None:
        params_list = (
            Test.Params(50, 10, 5),
            Test.Params(50, 10, 6),
            Test.Params(50, 10, 7),
            Test.Params(50, 10, 8),
            Test.Params(50, 10, 9),
            Test.Params(101, 15, 7),
            Test.Params(101, 15, 8),
        )

        for params in params_list:
            with self.subTest(params=str(params)):
                np.random.seed(0)
                x = np.random.rand(params.n)
                actual = real_stft(x, params.segment, params.overlap)
                _, _, expected = stft(
                    x,
                    boundary=None,
                    nperseg=params.segment,
                    noverlap=params.overlap,
                    padded=False,
                    window="boxcar",
                )
                assert isinstance(expected, np.ndarray)
                self.assertTrue(np.allclose(actual, params.segment * expected))


def main() -> None:
    try:
        # Загрузка WAV-файла
        fs, x = wavfile.read('6413-14.wav')
        
        # Конвертация в моно, если стерео
        if len(x.shape) > 1:
            x = x.mean(axis=1)
        
        # Нормализация
        x = x / np.max(np.abs(x))

        # Вычисление КВПФ с использованием scipy
        f, t, spectrum = stft(
            x,
            fs=fs,
            nperseg=1024,
            noverlap=512,
            window='boxcar',
            scaling='spectrum'
        )

        # Ограничиваем диапазон частот
        freq_min, freq_max = 100, 1000
        mask = (f >= freq_min) & (f <= freq_max)
        f = f[mask]
        spectrum = spectrum[mask, :]
        
        # Построение спектрограммы
        plt.figure(figsize=(14, 6))
        plt.pcolormesh(t, f, np.abs(spectrum)**2, shading='gouraud')
        ax = plt.gca()

        # Частотная ось (Y)
        ax.set_ylim(freq_min, freq_max)
        ax.yaxis.set_major_locator(MultipleLocator(100))  # Основные деления каждые 100 Гц
        ax.yaxis.set_minor_locator(MultipleLocator(25))    # Вспомогательные каждые 25 Гц

        # Временная ось (X)
        ax.xaxis.set_major_locator(MultipleLocator(0.5))  # Основные деления каждые 0.5 сек
        ax.xaxis.set_minor_locator(MultipleLocator(0.1))  # Вспомогательные каждые 0.1 сек

        # Добавление сетки
        ax.grid(which='major', linestyle='-', linewidth=0.5, alpha=0.7)
        ax.grid(which='minor', linestyle=':', linewidth=0.5, alpha=0.5)

        plt.colorbar(label='Амплитуда')
        plt.xlabel('Время [сек]')
        plt.ylabel('Частота [Гц]')
        plt.title('Спектрограмма')
        plt.tight_layout()
        plt.show()

    except FileNotFoundError:
        print("WAV-файл не найден. Пропускаем визуализацию спектрограммы.")


if __name__ == "__main__":
    #unittest.main()
    main()

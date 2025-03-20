import numpy as np
import matplotlib.pyplot as plt
from scipy import signal as sig
from scipy.io.wavfile import write

def tone(f, t, waveform='harmonic', fs=44100):
    # Генерация временной оси
    t = np.linspace(0, t, int(fs * t), endpoint=False)
    
    # Генерация тона в зависимости от выбранной формы
    if waveform == 'harmonic':
        signal = np.sin(2 * np.pi * f * t)
    elif waveform == 'square':
        signal = sig.square(2 * np.pi * f * t)
    elif waveform == 'triangle':
        signal = sig.sawtooth(2 * np.pi * f * t, width=0.5)
    elif waveform == 'sawtooth':
        signal = sig.sawtooth(2 * np.pi * f * t)
    else:
        raise ValueError("Неподдерживаемая форма сигнала. Используйте 'harmonic', 'square', 'triangle' или 'sawtooth'")
    
    return signal


def musical_tone(f, t, waveform='harmonic', fs=44100, db=-5):
    if db > 0:
        raise ValueError("Уровень затухания должен быть неположительным числом")

    ts = np.linspace(0, t, int(fs * t), endpoint=False)
    
    freqs = [f * (i + 1) for i in range(int(20000 / f))]
    amps = [1] + [0.5, 0.3, 0.2, 0.1][:len(freqs)-1]
    signal = np.zeros(len(ts))

    for freq, amp in zip(freqs, amps):
        signal += amp * tone(freq, t, waveform, fs)

    max_amp = np.max(np.abs(signal))
    if max_amp > 0:
        signal /= max_amp

    # Постепенное затухание
    decay_time = t  # Общее время затухания
    decay_samples = int(fs * decay_time)  # Количество образцов для затухания
    decay_env = np.linspace(1, 10 ** (db / 20), decay_samples)  # Создание экспоненциального затухающего огибающего

    # Применение затухания к сигналу
    if decay_samples < len(signal):
        signal[:decay_samples] *= decay_env
    else:
        signal *= decay_env[:len(signal)]

    return signal


if __name__ == '__main__':
    # Task 1
    # Генерация чистого тона
    generated_signal = tone(440, 2)

    # Визуализация
    plt.figure(figsize=(10, 4))
    plt.stem(generated_signal[:100])  # Показываем первые 100 отсчетов
    plt.title(f'Гармонический тон')
    plt.xlabel('Номер отсчета')
    plt.ylabel('Амплитуда')
    plt.grid()
    plt.show()

    # Task 2
    # Генерация затухающего составного тона
    generated_signal = musical_tone(440, 2)

    # Визуализация
    plt.figure(figsize=(10, 4))
    plt.plot(generated_signal[:1000])  # Показываем первые 1000 отсчетов
    plt.title('Затухающий составной тон')
    plt.xlabel('Номер отсчета')
    plt.ylabel('Амплитуда')
    plt.grid()
    plt.show()

    # Task 3
    # Словарь с частотами нот
    freqs = {
        'C5': 523, 
        'D5': 587, 
        'E5': 659, 
        'F#5': 740, 
        'G5': 784, 
        'A5': 880, 
        'B5': 988, 
        'C6': 1047, 
        'D6': 1175
    }
    
    # Параметры
    fs = 44100
    db = -1
    music_duration = 7  # Общая длительность музыкального произведения в секундах
    note_duration = 0.138  # Длительность одной ноты в секундах

    # Последовательнсть воспроизводимых нот
    sequence = ['E5', 'F#5', 'G5', 'A5', 'G5', 'F#5', 'A5', 'B5', 'C6', 'D6', 'C6', 'B5',
                'F#5', 'G5', 'A5', 'B5', 'A5', 'G5', 'G5', 'A5', 'B5', 'C6', 'B5', 'A5',
                'E5', 'F#5', 'G5', 'A5', 'G5', 'F#5', 'A5', 'B5', 'C6', 'D6', 'C6', 'B5',
                'C5', 'D5', 'E5', 'F#5', 'G5', 'A5', 'B5', 'A5', 'B5', 'A5', 'G5', 'F#5']
    
    total = music_duration * fs
    music = np.zeros(total)

    # Генерация и комбинирование фрагментов
    for i, note in enumerate(sequence):
        freq = freqs[note]
        fragment = musical_tone(freq, note_duration, 'triangle', fs, db)

        # Сдвиг фрагмента по времени
        start_sample = i * int(note_duration * fs)

        # Слияние фрагмента с музыкальным произведением
        music[start_sample:start_sample + len(fragment)] += fragment

    write('Oath_Of_Silence.wav', fs, np.float32(music))
    print("Музыкальное произведение создано и сохранено как 'Oath_Of_Silence.wav'")

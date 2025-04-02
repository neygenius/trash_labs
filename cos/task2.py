import numpy as np
from scipy.io.wavfile import write
from scipy import signal
import matplotlib.pyplot as plt


def musical_tone(f, t, waveform='harmonic', fs=44100, db=-20):
    if db > 0:
        raise ValueError("Уровень затухания db должен быть неположительным числом.")

    samples = np.linspace(0, t, int(fs * t), endpoint=False)

    signal_values = np.zeros_like(samples)
    num_overtones = 0
    while True:
        num_overtones += 1
        frequency = f * num_overtones
        if frequency > 20000:
            break

        amplitude = 1 / num_overtones # Амплитуда обертона

        if waveform == 'harmonic':
            tone = np.sin(2 * np.pi * frequency * samples)
        elif waveform == 'square':
            tone = signal.square(2 * np.pi * frequency * samples)
        elif waveform == 'triangle':
            tone = signal.sawtooth(2 * np.pi * frequency * samples, width=0.5)
        elif waveform == 'sawtooth':
            tone = signal.sawtooth(2 * np.pi * frequency * samples)
        else:
            raise ValueError("Неподдерживаемая форма сигнала. Используйте 'harmonic', 'square', 'triangle' или 'sawtooth'.")

        signal_values += amplitude * tone

    signal_values = signal_values / np.max(np.abs(signal_values))

    if db < 0:
        alpha = 10 ** (db / 20)
        decay = alpha ** (samples / t)
        signal_values *= decay

    return signal_values


f = 440
t = 2
fs = 44100
db = -30

signal_values = musical_tone(f, t, waveform='harmonic', fs=fs, db=db)

plt.figure(figsize=(10, 4))

plt.plot(np.linspace(0, t, int(fs * t)), signal_values)
plt.title('Затухающий составной тон')
plt.xlabel('Время (с)')
plt.ylabel('Амплитуда')
plt.grid()

plt.show()

write("musical_tone.wav", fs, signal_values)
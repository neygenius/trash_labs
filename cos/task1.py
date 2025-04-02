import numpy as np
import matplotlib.pyplot as plt
from scipy import signal as sig
from scipy.io.wavfile import write


def tone(f, t, waveform='harmonic', fs=44100):
    samples = np.linspace(0, t, int(fs * t), endpoint=False)
    
    if waveform == 'harmonic':
        signal = np.sin(2 * np.pi * f * samples)
    elif waveform == 'square':
        signal = sig.square(2 * np.pi * f * samples)
    elif waveform == 'triangle':
        signal = sig.sawtooth(2 * np.pi * f * samples, width=0.5)
    elif waveform == 'sawtooth':
        signal = sig.sawtooth(2 * np.pi * f * samples)
    else:
        raise ValueError("Неподдерживаемая форма сигнала. Используйте 'harmonic', 'square', 'triangle' или 'sawtooth'")
    
    return signal


f = 440
t = 2
fs = 44100

harmonic_tone = tone(f, t, waveform='harmonic', fs=fs)
square_tone = tone(f, t, waveform='square', fs=fs)
triangle_tone = tone(f, t, waveform='triangle', fs=fs)
sawtooth_tone = tone(f, t, waveform='sawtooth', fs=fs)

plt.figure(figsize=(12, 8))

plt.subplot(4, 1, 1)
plt.stem(np.linspace(0, 0.005, int(fs * 0.005)), harmonic_tone[:int(fs * 0.005)])
plt.title('Гармонический сигнал')
plt.xlabel('Время (с)')
plt.ylabel('Амплитуда')

plt.subplot(4, 1, 2)
plt.stem(np.linspace(0, 0.005, int(fs * 0.005)), square_tone[:int(fs * 0.005)])
plt.title('Меандр со скважностью 2')
plt.xlabel('Время (с)')
plt.ylabel('Амплитуда')

plt.subplot(4, 1, 3)
plt.stem(np.linspace(0, 0.005, int(fs * 0.005)), triangle_tone[:int(fs * 0.005)])
plt.title('Треугольный сигнал')
plt.xlabel('Время (с)')
plt.ylabel('Амплитуда')

plt.subplot(4, 1, 4)
plt.stem(np.linspace(0, 0.005, int(fs * 0.005)), sawtooth_tone[:int(fs * 0.005)])
plt.title('Пилообразный сигнал')
plt.xlabel('Время (с)')
plt.ylabel('Амплитуда')

plt.tight_layout()
plt.show()

write('harmonic_tone.wav', fs, np.float32(harmonic_tone))
write('square_tone.wav', fs, np.float32(square_tone))
write('triangle_tone.wav', fs, np.float32(triangle_tone))
write('sawtooth_tone.wav', fs, np.float32(sawtooth_tone))

import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write
from task2 import musical_tone

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

music = np.zeros(music_duration * fs)

# Генерация и комбинирование фрагментов
for i, note in enumerate(sequence):
    frequency = freqs[note]
    fragment = musical_tone(frequency, note_duration, 'triangle', fs, db)

    # Сдвиг фрагмента по времени
    start_sample = i * int(note_duration * fs)

    # Слияние фрагмента с музыкальным произведением
    music[start_sample:start_sample + len(fragment)] += fragment

write('Oath_Of_Silence.wav', fs, np.float32(music))

plt.figure(figsize=(10, 4))
plt.plot(np.linspace(0, len(music) / fs, len(music)), music)
plt.title('Фрагмент партии из "Oath_Of_Silence"')
plt.xlabel('Время (с)')
plt.ylabel('Амплитуда')
plt.grid()
plt.show()
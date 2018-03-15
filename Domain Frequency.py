from scipy.io import wavfile
from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
import peakutils

rate, audio = wavfile.read('normal.wav')

M = 1024

freqs, times, Sx = signal.spectrogram(audio, fs=rate, window='hanning',
                                      nperseg=1024, noverlap=M - 10,
                                      detrend=False, scaling='spectrum')
f, ax = plt.subplots(figsize=(4.8, 2.4))
ax.pcolormesh(times, freqs, 10 * np.log10(Sx), cmap='viridis')
ax.set_ylabel('Frequency [Hz]')
ax.set_xlabel('Time [s]')
plt.show()

print(times)
from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt


def time(arrayAudio, rate):

    #audio = np.mean(audio, axis=1)

    N = arrayAudio.shape[0]
    L = N / rate

    print('Audio length: %.2f seconds'%L)

    f, ax = plt.subplots()
    ax.plot(np.arange(N) / rate, arrayAudio)
    ax.set_xlabel('Time [s]')
    ax.set_ylabel('Amplitude [unknown]')
    plt.show()

from collections import OrderedDict
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy.io import wavfile
import numpy.fft
numpy.set_printoptions(threshold=numpy.nan)
rate, data = wavfile.read('normal.wav')

print("Frequência: " + str(rate))
print("Dados:")
print(data)
print(len(numpy.abs(data)))


fourier = numpy.fft.fft(data)
print("Dados Fourier")
print(numpy.abs(fourier))
print(len(numpy.abs(fourier)))
print(len(list(dict.fromkeys(numpy.abs(fourier)))))

fig = plt.figure()
fig.suptitle('Transformada rápida de Fourier', fontsize='medium')
ax = fig.add_subplot(211)
ax.plot(data)
ax.set_title('Normal')
ax = fig.add_subplot(212)
ax.plot(numpy.abs(fourier))
ax.set_title('Fourier',fontsize='medium')
plt.subplots_adjust(hspace=0.5, wspace=1.0)
plt.show()
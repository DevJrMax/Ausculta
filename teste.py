import libs.wavio as wavio
import libs.fingerprint as fingerprint
import plotDomain

import numpy as np

rate,sampWidth,audio,channels = wavio.readwav("normal.wav")
print("Sample Rate:"+str(rate))
print("Sample Width:"+str(sampWidth))
print("Array from audio:"+str(audio))
print("Number of channels:"+str(channels))

plotDomain.time(audio, rate)


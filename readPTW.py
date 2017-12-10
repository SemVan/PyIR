from pyradi import ryptw
from matplotlib import pyplot as plt
import numpy as np

def write_file(fileName, array):
    with open(fileName, 'w') as file:
        for elem in array:
            file.write(str(elem))
            file.write('\n')
    return

def get_fourier_result (signal, period):
    complex_four = np.fft.fft(signal)
    spectra = np.absolute(complex_four)
    freqs = []
    for i in range(len(signal)):
        freqs.append(1/(period*len(signal))*i)
    return spectra, freqs

head = ryptw.readPTWHeader("Capture024.ptw")
# ryptw.showHeader(head)
signal = []
for i in range(1, 2100):
    frame = ryptw.getPTWFrame(head, i)
    r_frame = frame[0]
    print(i)
    signal.append(np.ndarray.mean(r_frame))
write_file("signal.txt", signal)
plt.plot(range(len(signal)), signal)
plt.show()

four, freqs = get_fourier_result(signal, 1/115)
plt.plot(freqs, four)
plt.show()

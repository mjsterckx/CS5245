import numpy as np
from scipy.io.wavfile import read, write
import matplotlib.pyplot as plt

rate, data = read('speech.wav')
data = list(data)

new_data = []
for d in data:
    new_data.append(min(max(2 * d, -32768), 32767))

print("The clipped range is (" + str(min(new_data)) + ", " + str(max(new_data)) + ").")

x = []
for i in range(0, len(data)):
    x.append(float(len(data) / rate) * (i / len(data)))
plt.plot(x, new_data)
plt.xlabel('time (seconds)')
plt.show()

new_data = np.array(new_data)
write('speech_clipped.wav', rate, new_data)

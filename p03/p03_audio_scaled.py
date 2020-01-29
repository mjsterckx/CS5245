from scipy.io.wavfile import read
import matplotlib.pyplot as plt

rate, data = read('speech.wav')
data = list(data)
print("The original range is (" + str(min(data)) + ", " + str(max(data)) + ").")

new_data = []
for d in data:
    new_data.append(2 * d)

print("The new range is (" + str(min(new_data)) + ", " + str(max(new_data)) + ").")

x = []
for i in range(0, len(data)):
    x.append(float(len(data) / rate) * (i / len(data)))
plt.plot(x, new_data)
plt.xlabel('time (seconds)')
plt.show()

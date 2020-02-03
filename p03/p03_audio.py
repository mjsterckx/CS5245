from scipy.io.wavfile import read, write
import matplotlib.pyplot as plt

rate, data = read('speech.wav')
data = list(data)
print("There are " + str(len(data)) + " samples.")
print("The sample rate is " + str(rate) + " samples/sec.")
print("The file is " + str(float(len(data) / rate)) + " seconds long.")

x = []
for i in range(0, len(data)):
    x.append(float(len(data) / rate) * (i / len(data)))

plt.plot(x, data)
plt.xlabel('time (seconds)')
plt.show()

import p04

rate, data = p04.load('speech.wav')
times = p04.get_times(len(data), 0, rate)
x, y = p04.zoom(times, data, 87300, 150)
scaled = p04.clip(p04.scale(y, 5))
p04.save('wash.wav', rate, scaled)
rate, data = p04.load('wash.wav')
plt = p04.plot_audio(x, data, 'wash')
plt.show()

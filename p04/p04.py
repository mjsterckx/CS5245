def load(file_name):
    from scipy.io.wavfile import read
    rate, data = read(file_name)
    data = list(data)
    return rate, data


def save(file_name, rate, data):
    from numpy import array
    from scipy.io.wavfile import write
    data = array(data, dtype='int16')
    write(file_name, rate, data)


def get_times(num_samples, start_time, sample_rate):
    x = []
    for n in range(num_samples):
        x.append(start_time + n * (1 / sample_rate))
    return x


def scale(y, alpha):
    new_y = []
    for i in y:
        new_y.append(alpha * i)
    return new_y


def clip(y):
    new_y = []
    for i in y:
        new_y.append(min(max(i, -32768), 32767))
    return new_y


def zoom(x, y, start, n):
    x2 = []
    y2 = []
    for i in range(n):
        x2.append(x[start + i])
        y2.append(y[start + i])
    return x2, y2


def double_pitch(y):
    y2 = []
    for i in range(0, len(y), 2):
        y2.append(y[i])
    return y2


def half_pitch(y):
    y2 = []
    for i in y:
        y2.append(i)
        y2.append(i)
    return y2


def plot_audio(x, y, title):
    import matplotlib.pyplot as plt
    plt.plot(x, y)
    plt.xlabel('Time (seconds)')
    plt.ylabel('Amplitude')
    plt.title(title)
    plt.savefig(title + '.png')
    return plt

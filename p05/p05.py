import pandas as pd
import matplotlib.pyplot as plt
from time import time


def bmi(file_name):
    df = pd.read_csv(file_name)
    height = df['Height']
    weight = df['Weight']
    bmi = []
    for i in range(len(height)):
        bmi.append(703 * (weight[i] / (height[i] ** 2)))
    df['BMI'] = bmi
    df.to_csv(file_name[:-4] + '_bmi.csv', index=False)


def plot_signals(file_name):
    df = pd.read_csv(file_name)
    columns = list(df.columns)
    x_coor = df['x']
    y_coor_1 = df[columns[1]]
    y_coor_2 = df[columns[2]]
    y_coor_3 = df[columns[3]]
    line1, = plt.plot(x_coor, y_coor_1, color='g', linestyle='--', linewidth=2, marker='o', label=columns[1])
    line2, = plt.plot(x_coor, y_coor_2, color='c', linestyle=':', linewidth=2, marker='+', label=columns[2])
    line3, = plt.plot(x_coor, y_coor_3, color=(1.0, 0.5, 0.0), linestyle='-.', linewidth=2, marker='D', label=columns[3])
    plt.legend([line1, line2, line3], [columns[1], columns[2], columns[3]])
    plt.xlabel('time')
    plt.ylabel('amplitude')
    plt.title(file_name[:-4] + '_plot.png')
    plt.savefig(file_name[:-4] + '_plot.png')


def grade_hist(file_name):
    df = pd.read_csv(file_name)
    bins = range(0, 101, 5)
    plt.hist(df['Grades'], bins=bins, edgecolor='black')
    plt.xlabel('Grade')
    plt.ylabel('Count')
    plt.title(file_name[:-4] + '_hist.png')
    plt.savefig(file_name[:-4] + '_hist.png')


def time_it(a, n, value=-1):
    contained = False
    total_time = 0
    for i in range(n):
        start_time = time()
        contained = value in a
        total_time += (time() - start_time)
    return total_time / n

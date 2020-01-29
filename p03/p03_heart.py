import math
import matplotlib.pyplot as plt

n = int(input("Enter number of edges: "))
theta = []
for i in range(n + 1):
    theta.append(float((i * 2 * math.pi) / n))

x = []
y = []
for t in theta:
    x.append(16 * (math.sin(t) ** 3))
    y.append(13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t))

plt.plot(x, y)
plt.axis('square')
plt.show()

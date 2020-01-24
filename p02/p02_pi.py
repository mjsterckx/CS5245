from random import uniform

n = int(input("Enter n: "))
in_circle = 0
for i in range(0, n):
    x = uniform(-1, 1)
    y = uniform(-1, 1)
    diagonal = (x ** 2 + y ** 2) ** (1/2)
    if diagonal <= 1:
        in_circle += 1
pi_approx = float(in_circle / n) * 4
print("After " + str(n) + " trials, the approximation is pi = " + str(pi_approx) + ".")

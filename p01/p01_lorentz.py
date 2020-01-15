s = float(input('Enter the velocity (m/s): '))
c = 3 * (10 ** 8)
lorentz = 1 / ((1 - (s ** 2 / c ** 2)) ** (1 / 2))
print('The Lorentz factor at', s, 'm/s is', str(lorentz) + '.')

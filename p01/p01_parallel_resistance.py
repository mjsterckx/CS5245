r1 = float(input('Enter r1: '))
r2 = float(input('Enter r2: '))
r3 = float(input('Enter r3: '))
rt = 1 / (1 / r1 + 1 / r2 + 1 / r3)
print('The parallel resistance of ' + str(r1) + ', ' + str(r2) + ', and', str(r3), 'ohms is', str(rt), 'ohms.')

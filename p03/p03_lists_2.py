from random import randint
n = int(input("Enter n: "))
l = []
for i in range(n):
    l.append(randint(1, 10))
print("The minimum is " + str(min(l)) + ".")
print("The maximum is " + str(max(l)) + ".")
print("The sum is " + str(sum(l)) + ".")
print("The average is " + str(float(sum(l) / n)) + ".")

n = int(input("Enter n: "))
result = 1
for i in range(1, n + 1):
    previous = result
    result = result * i
    print(str(i) + " x " + str(previous) + " = " + str(result))
print(str(n) + "! = " + str(result))

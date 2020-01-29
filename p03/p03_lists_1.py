a = [1, 2, 3, 4]
print(a)
a.append(10)
print(a)
print("The minimum is " + str(min(a)) + ".")
print("The maximum is " + str(max(a)) + ".")
print("The sum is " + str(sum(a)) + ".")
b = ['a', 'b', 'c']
print(b)
for i in b:
    a.append(i)
print(a)
print(a[4])
print(a[4:7])
a[4] = 20
print(a)

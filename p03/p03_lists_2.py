from random import randint
n = int(input("Enter n: "))
list_n = []
for i in range(n):
    list_n.append(randint(1, 10))
print("The list is: " + str(list_n) + ".")
print("The minimum is " + str(min(list_n)) + ".")
print("The maximum is " + str(max(list_n)) + ".")
print("The sum is " + str(sum(list_n)) + ".")
print("The average is " + str(float(sum(list_n) / n)) + ".")

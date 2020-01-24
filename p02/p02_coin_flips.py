from random import randint

times_correct = 0
for i in range(0, 10):
    coin = randint(1, 2)
    guess = int(input("Enter your guess (1 or 2): "))
    if guess == coin:
        times_correct += 1
        print("You are correct " + str(guess) + " == " + str(coin) + ".")
    else:
        print("Sorry, " + str(guess) + " != " + str(coin) + ".")
print("You were correct " + str(times_correct) + " times.")

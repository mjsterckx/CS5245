import turtle as t

n = int(input("Enter amount of sides: "))

t_shape = t.Turtle()
for i in range(n):
    t_shape.forward(100)
    t_shape.right(360/n)

input("")

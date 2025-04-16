import turtle

Guess = int(input("What is 2 X 7?"))

# Set up the screen
wn = turtle.Screen()
wn.title("Turtle Drawing with User Input")
wn.bgcolor("lightyellow")

tina = turtle.Turtle()

if Guess == 2*7:
    tina.write(str(Guess) + ' is correct!')
    tina.penup()
    tina.backward(10)
else:
    tina.write('You said ' + str(Guess) + '. I got ' + str(2*7))
    tina.penup()
    tina.backward(10)

# Keep the window open
wn.mainloop()
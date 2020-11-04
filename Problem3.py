#Raymundo Sanchez
#Oct 30,2020

# the import turtle is here since you will need it to draw and for anything here to even work
import turtle


t = turtle.Turtle()

#this asks the person what they want the length of the Hexagon to be.
#the "side" just means that it's the sides of the Hexagon incase you don't remember.
side = int(input("What length do you want the Hexagon to have: "))

#Here it will ask you what color you want the Hexagon to be and add your response.
color = input("What color do you want your Hexagon: ")

#this helps the color actually work with what color you choose.
t.fillcolor(color)

#this will make it so it starts to paint the Hexagon from the inside
t.begin_fill()

#this will draw out the sides of the Hexagon after it gets the length you choose
#it will also tell it what sides it need to move
for _ in range(6):
    t.forward(side)
    t.right(-60)

#this just stops coloring the Hexagon and then it's done
t.end_fill()





import time
import random
load_done = False
fairydust = 0
fairydust_msg = False
fd_amount = 0   #(amount that is increased or decreased by. + or -)
travelling = False
print("<Fairy>  Oh! Hello there :>")
time.sleep(0.1)
print("You seem a bit lost. Let me teleport you to where you should be :)")
time.sleep(0.1)
print("Say: Okay, I\'m ready!  (a)  |  OR:  Who are you?  (b)")
time.sleep(0.1)
print("=======================================================")
response = input ("Choice (a) or (b)?")
if response == "a":
    print("<Fairy>  Okay, get ready--close your eyes!!")
    time.sleep(0.1)
    print("<You close your eyes... and open your eyes to a different world>")
if response == "b":
    print("<Fairy>  I am Tilly. I am your fairy godmother :>  Go make me proud!")
    time.sleep(0.1)
    print("Fairy Godmother gave you 5 fairydust!!")
    #fairydust += 5
    fairydust_msg = True
    fd_amount += 5
    from = "FG"
    print("<Fairy Godmother>  Off with you, now, little one! Don\'t lose my fairydust!>")
import turtle
screen = turtle.Screen()
travelling = True
t = turtle.Turtle()
p = turtle.Turtle()
fd = turtle.Turtle()  #fd for fairydust

t.color("green")
width = screen.window_width()
height = screen.window_height()
u_max = height / 2
d_max = height / 2 * -1
p_max = width / 2
n_max = width / 2 * -1
header_y = (u_max / 5) * 4
header = (0, header_y)
footer_y = (d_max / 5) * 4 *-1
footer = (0, footer_y)







while True:
    if travelling == True:
        load_done = False
        screen.title("Teleporting to Fairy Land...")
        screen.bgcolor("black")
        t.shapesize(stretch_wid = 1, stretch_len = 1.5, outline = 1)
        t.speed(2)
        t.shape("circle")
        t.pencolor("pink")
        t.color("green")
        t.showturtle()
        t.penup()
        t.goto(0, 0)
        #t.color("pink")
        t.dot(5, "pink")
        t.goto(15, 20)
        t.dot(4, "green")
        t.goto(20, 15)
        t.dot(3, "yellow")
        t.goto(-20, 15)
        t.dot(2, "orange")
        t.goto(-15, 20)
        t.dot(1, "purple")
        load_done = True
    #if travelling == False:
    if fairydust_msg == True:
        t.hideturtle()
        t.goto(footer)
        t.write("<from " + from + ">  + " + str(fd_amount) + " fairydust", align = "right", font = ("Courier New", 15, "italic"))
        fd_amount = 0
        fairydust += 5
        fd.write("fd." + str(fairydust) + ".m." + str(magic) + ".", align = "right", font = ("Verdana", 5, "bold"))

#fd_amount = fairydust_amount but quicker to type.
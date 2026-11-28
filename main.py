import time
import random
load_done = False
fairydust = 0
fairydust_msg = False
fd_amount = 0   #(amount that is increased or decreased by. + or -)
travelling = False
store_open = False
store_sv = 0 #sv stands for session visits. 0/3 until next 5-min store-open/closed-refresh.
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
    from1 = "FG"
    print("<Fairy Godmother>  Off with you, now, little one! Don\'t lose my fairydust!>")
import turtle
screen = turtle.Screen()
travelling = True
active = False
zzz = False

store_working = True

q = turtle.Turtle()  #random work for the game
t = turtle.Turtle()
p = turtle.Turtle()
fd = turtle.Turtle()  #fd for fairydust
m = turtle.Turtle()  #merchant-fairy-turtle

t.color("green")
width = screen.window_width()
height = screen.window_height()
u_max = height / 2
d_max = height / 2 * -1
p_max = width / 2
n_max = width / 2 * -1
header_y = (u_max / 5) * 4
header = (0, header_y)
footer_y = (d_max / 5) * 4
footer = (0, footer_y)
dr_corner = (p_max, d_max)  #down-right corner (bottom-right corner)
stats_corner = (p_max, footer_y) #close by dr_corner but a bit elevated on y-axis so it will be noticed better
#more variables!
shop_corner = (n_max + 50, u_max - 50)
magic = 0 #magic amount or level of magic. Total needed = 8 for now..?

p.hideturtle()
p.speed(2)
p.shapesize(stretch_wid = 0.2, stretch_len = 1, outline = 1)
p.shape("circle")
p.pencolor("green")
p.color("blue")


def left():
    global active
    global zzz
    zzz = False
    active = True
    p.showturtle()
    p.setheading(0)
    screen.tracer(0)
    p.right(180)
    screen.tracer(1)
    p.forward(50)
    active = False

def right():
    global active
    global zzz
    zzz = False
    active = True
    p.showturtle()
    p.setheading(0)
    p.forward(50)
    active = False

def up():
    global active
    global zzz
    zzz = False
    active = True
    p.showturtle()
    p.setheading(0)
    screen.tracer(0)
    p.left(90)
    screen.tracer(1)
    p.forward(50)
    active = False

def down():
    global active
    global zzz
    zzz = False
    active = True
    p.showturtle()
    p.setheading(0)
    screen.tracer(0)
    p.right(90)
    screen.tracer(1)
    p.forward(50)
    active = False

def shop_refresh():
    global store_sv
    global store_working
    q.clear()  #so the store-notif msg only ends up staying for a few seconds
    m.showturtle()
    m.penup()
    m.goto(shop_corner)
    m.shapesize(stretch_wid = 5, stretch_len = 5, outline = 2)
    if store_sv <= 0: #error
        m.color("red")
        m.write("Error", align = "center", font = ("Impact", 5, "italic"))
        store_working = False
    if store_sv >= 0:
        m.color("orange")
        m.pencolor("gray")
        m.write(store_sv + "/3 visits", align = "center", font = ("Courier New", 5, "normal"))
        store_working = True
    if store_sv > 3:
        m.color("red")
        m.write("Store locked. Wait 5 mins!", align = "center", font = ("Courier New", 5, "normal"))
        store_working = False
    else:  #if store_sv == 0:
        m.color("green")
        m.write("Store open!", align = "center", font = ("Courier New", 5, "normal"))
        store_working = True
    if store_working == True:
        if p.distance(m) <= 5:
            def open_store():
                t.penup()
                t.goto(header)
                t.write("travelling...")
                title_update = True
                def window_status():
                    screen.Title("Travelling to shop...")
                    screen.bgcolor("brown")
                    m.hideturtle()
                    m.penup()
                    m.goto(header)
                    m.color("white")
                    m.pencolor("white")
                    m.write("Press 1-8 (top-bottom) to purchase a wand. No refunds.", align = "center", font = ("Verdana", 20, "underline"))
                    m.setheading(0)
                    m.right(90)
                    m.forward(70)
                    m.write("Sample Wand: 0 fairydust", align = "center", font = ("Courier New", 15, "normal"))
                    m.setheading(0)
                    m.right(90)
                    m.forward(50)
                    m.write("Starter Wand: 10 fairydust", align = "center", font = ("Courier New", 15, "normal"))
                    m.setheading(0)
                    m.right(90)
                    m.forward(50)
                    m.write("Novice Wand: 18 fairydust", align = "center", font = ("Courier New", 15, "normal"))
                    m.setheading(0)
                    m.right(90)
                    m.forward(50)
                    m.write("Junior Wand: 25 fairydust", align = "center", font = ("Courier New", 15, "normal"))
                    m.setheading(0)
                    m.right(90)
                    m.forward(50)
                    m.write("Professional Wand: 40 fairydust", align = "center", font = ("Courier New", 15, "normal"))
                    m.setheading(0)
                    m.right(90)
                    m.forward(50)
                    m.write("Senior Wand: 65 fairydust", align = "center", font = ("Courier New", 15, "normal"))
                    m.setheading(0)
                    m.right(90)
                    m.forward(50)
                    m.write("Expert Wand: 80 fairydust", align = "center", font = ("Courier NEw", 15, "normal"))
                    m.setheading(0)
                    m.right(90)
                    m.forward(50)
                    m.write("Supernatural Wand: 100 fairydust", align = "center", font = ("Impact", 15, "italic"))

#animations
def sleepy():
    global zzz
    global active
    active = False
    zzz = True
def sleep():
    global zzz
    global active
    active = False
    if zzz == True:
        p.speed(1)
        p.shapesize(stretch_wid = 1, stretch_len = 0.2, outline = 1.5)
        p.shape("circle")
        p.pencolor("green")
        p.color("white")
        p.speed(2)
        p.showturtle()

screen.onkey(left, "Left")
screen.listen()
screen.onkey(right, "Right")
screen.listen()
screen.onkey(up, "Up")
screen.listen()
screen.onkey(down, "Down")
screen.listen()

#maintenance
def script_clearer():
    fd.clear()

def trail_clearer():
    p.clear()
#timers
def trail_clear():
    screen.ontimer(trail_clearer, 1500)

def shop_notif():
    q.penup()
    q.goto(footer)
    q.write("Store will open in 1 minute", align = "center", font = ("Verdana", 10, "underline"))


screen.ontimer(script_clearer, 3000)
screen.ontimer(zzz, 15000) #every 15 seconds, p-turtle/fairy goes zzz. Most fairies don't sleep so often. Don't get caught as a not-true-fairy!
screen.ontimer(shop_refresh, 300000)  #every 5 mins: store function triggerd (store opens.)
screen.ontimer(shop_notif, 288000)  #every 4.8 mins; for store notif/alert

while True:
    trail_clear()  #clears p-turtle's trail every 1.5 seconds.
    if travelling == True:
        load_done = False
        screen.title("Teleporting to Fairy Land...")
        screen.bgcolor("black")
        p.hideturtle()
        p.clear()
        t.shapesize(stretch_wid = 0.2, stretch_len = 1, outline = 1)
        t.speed(2)
        t.shape("circle")
        t.pencolor("green")
        t.color("pink")
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
        t.clear()
        t.hideturtle()
        time.sleep(1.5)
        travelling = False
    #if travelling == False:
    if fairydust_msg == True:
        t.hideturtle()
        t.goto(footer)
        t.write("<from " + from1 + ">  + " + str(fd_amount) + " fairydust", align = "right", font = ("Courier New", 15, "italic"))
        fd_amount = 0
        fairydust += 5
        fd.goto(stats_corner)
        fd.write("fd." + str(fairydust) + ".m." + str(magic) + ".", align = "right", font = ("Verdana", 5, "bold"))
        fairydust_msg = False
    if fairydust_msg == False:
        t.clear()
        fd.clear()

#fd_amount = fairydust_amount but quicker to type.
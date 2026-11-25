import time
import random
fairydust = 0
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
    fairydust += 5
    print("<Fairy Godmother>  Off with you, now, little one! Don\'t lost my fairydust!>")
import turtle
screen = screen.Turtle()
travelling = True
t = turtle.Turtle()
p = turtle.Turtle()

t.color("green")
width = 




while True:
    if travelling == True:
        screen.Title("Teleporting to Fairy Land...")
    if travelling == False:

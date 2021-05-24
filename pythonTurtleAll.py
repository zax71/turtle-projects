import turtle as t
import time

#functions
def rect(x, y, fcol, pcol):
    t.pendown()
    t.fillcolor(fcol)
    t.pencolor(pcol)
    t.begin_fill()
    t.fd(x)
    t.lt(90)
    t.fd(y)
    t.lt(90)
    t.fd(x)
    t.lt(90)
    t.fd(y)
    t.lt(90)
    t.end_fill()
    t.penup()

#polyunction
def polygon(angle, lineLen, sides):
    for i in range(0, sides):
        t.fd(lineLen)
        t.lt(angle)

#rectangle no fill
def rectNoFill(x, y):
    t.fd(x)
    t.lt(90)
    t.fd(y)
    t.lt(90)
    t.fd(x)
    t.lt(90)
    t.fd(y)
    t.lt(90)    



selection = input("what task do you want to run? (1, 2, 3, 4 ect) ")

if selection == "1":
    rect(100, 100, "brown", "red")
elif selection == "2":
    rect(180, 180, "blue", "purple")
elif selection == "3":
    rect(150, 80, "blue", "purple")
elif selection == "4":
    rect(150, 80, "blue", "purple")
    t.fd(100)
    rect(120, 190, "orange", "red")
elif selection == "5":
    polygon(120, 150, 3)
elif selection == "6":
    sel6 = input("what shape? (pentogon = 1, hexogon = 2, octogon = 3, decagon = 4) ")

    if sel6 == "1":
        polygon(72, 50, 5)
    elif sel6 == "2":
        polygon(60, 50, 6)
    elif sel6 == "3":
        polygon(45, 50, 8)
    elif sel6 == "4":
        polygon(36, 50, 10)
    else:
        print("DO A NUMBER I HAVE!!!!!!! I ALLREDY said it earlier, 1-4!!!!!!!!")

elif selection == "7":
    rect(100, 100, "white", "black")

elif selection == "8":
    print("it draws 2 squares")

    rect(100, 100, "white", "black")
    t.penup()
    t.fd(120)
    t.pendown()
    rect(100, 100, "white", "black")
    
elif selection == "9":
    t.penup()
    t.lt(180)
    t.fd(400)
    t.lt(180)
    t.pendown()
    for i in range(4):
        t.penup()
        t.fd(140)
        t.pendown()
        for i in range(4):
            t.fd(100)
            t.lt(90)

elif selection == "10":
    polygon(144, 100, 5)

elif selection == "11":
    t.penup()
    t.goto(-300, 0)
    t.pendown()
    for i in range(4):
        polygon(144, 100, 5)
        t.penup()
        t.fd(120)
        t.pendown()

elif selection == "12":
    polygon(198, 100, 20)

elif selection == "13":
    standard = input("do you want the standdard one? (y/n)")
    
    if standard == "n":
        
        size = input("how big do you want? (pick 9 for the standard project!)")
        D3 = input("do you want 3D? (y/n)")
        
        t.goto(0, 0)
        for i in range(0, int(size)):
            rectNoFill(i*10, i*10)

        if D3 == "y":
            t.setheading(t.towards(int(size), int(size)))
            t.fd(int(size)*10)
            t.penup()
            t.fd(40)
            t.pendown()


    else:
        for i in range(0, 9):
                rectNoFill(i*10, i*10)
elif selection == "14":
    print("this program makes a shape with angles of 30o with a configurable ammount of sides")
    print("2 & 3 are dealing with a variable to set the sides \n")

    sides = int(input("how many sides?"))
    t.pencolor("red")
    polygon(30, 50, sides)

elif selection == "15":
    sides = int(input("how many sides?"))
    color = input("what colour?")
    t.pencolor(color)
    polygon(30, 50, sides)

elif selection == "16":
    for i in range(5):
        print((i+3-2)*180/(i+3))

elif selection == "17":
    angle = 0
    sides = int(input("number of sides"))
    
    angle = (angle - 2)*180/sides
    
    polygon(angle, 50, sides)
else:
    print("type a number that i have ya numpty")
    

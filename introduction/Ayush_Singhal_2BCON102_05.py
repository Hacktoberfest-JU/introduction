#MY NAME IS AYUSH SINGHAL
#THIS CODE CONSISTS VISUAL REPRESENTATIONS OF SOME FUNCTIONS OF TURTLE
def fd(a):#1
    import turtle 
    turtle.forward(a)
def bk(a):#2
    import turtle 
    turtle.backward(a)
def rt(a):#3
    import turtle 
    turtle.right(a)
def lt(a):#4
    import turtle 
    turtle.left(a)
def goto(a):#5
    import turtle 
    turtle.setposition(a)
def sx(a):#6
    import turtle 
    turtle.setx(a)
def sy(a):#7
    import turtle 
    turtle.sety(a)
def he(a):#8
    import turtle 
    turtle.home()
def circle(a):#9
    import turtle 
    turtle.circle(a)
def dot(a):#10
    import turtle 
    turtle.home(a)
def stamp():#11
    import turtle 
    turtle.stamp()
def clearstamp():#12
    import turtle 
    turtle.clearstamp()
def speed(a): #13
    import turtle 
    turtle.speed(a)
def pos(a):#14
    import turtle 
    turtle.position(a)
def xcor(a):#15
    import turtle 
    turtle.xcor(a)
def ycor(a):#16
    import turtle 
    turtle.ycor(a)
def heading():#17
    import turtle 
    turtle.heading()
def dis():#18
    import turtle 
    turtle.distance()
def pd():#19
    import turtle 
    turtle.pendown()
def pu():#20
    import turtle 
    turtle.penup()
def width(a):#21
    import turtle 
    turtle.pensize(a)
def pen():#22
    import turtle 
    turtle.pen()
def isd():#23
    import turtle 
    turtle.isdown()
def pro():#25
    import turtle 
    turtle.pencolor()
def ret():#26
    import turtle 
    turtle.reset()
def cr():#27
    import turtle 
    turtle.clear()
def we(a):#28
    import turtle 
    turtle.write(a)
def hide():#29
    import turtle 
    turtle.hideturtle()
def se():#30
    import turtle 
    turtle.showturtle()
def ie():#31
    import turtle 
    turtle.invisible()
def tilt(a):#32
    import turtle 
    turtle.tilt(a)
def tilt():#33
    import turtle 
    turtle.tilt()
def get_shapepoly():#34
    import turtle 
    turtle.get_shapepoly()
def clone():#36
    import turtle 
    turtle.clone()
def delay(a):#36
    import turtle 
    turtle.delay(a)
def turtles():#37
    import turtle 
    turtle.turtles()
def window_height():#38
    import turtle 
    turtle.window_height()
def window_width():#39
    import turtle 
    turtle.window_width()
def bye():#40
    import turtle 
    turtle.bye()
print("THIS FILE CONTAINS A VISUAL REPRESENTATION OF MOST OF THE TURTLE MODULE FUNCTIONS")
print("1. TO MOVE THE TURTLE FORWARD WITH A SPECIFIC AMOUNT")
print("2. TO MOVE THE TURTLE BACKWARD WITH A SPECIFIC AMOUNT")
print("3. TO MOVE THE HEAD OF THE TURTLE IN RIGHT WITH A SPECIFIC DEGREE")
print("4. TO MOVE THE HEAD OF THE TURTLE IN LEFT WITH A SPECIFIC DEGREE")
print("5. TO MOVE TURTLE TO A SPECIFIC POSITION (WORKS ONLY IN ONE DIRECTION)")
print("6. TO SET THE X COORDINATE OF THE TURTLE")
print("7. TO SET THE Y COORDINATE OF THE TURTLE")
print("8. TO MOVE THE TURTLE TO THE HOME(ORIGIN)")
print("9. TO MAKE A CIRCLE OF A RADIUS(R)")
print("10. TO MAKE A DOT WITH TURTLE OF A SPECIFIC THICKNESS")
print("11. TO MAKE A STAMP OF THE TURTLE LINE")
print("12. TO CLEAR A SPECIFIC STAMP OF THE TURTLE LINE")
print("13. TO SET THE MOVEMENT SPEED OF THE TURTLE LINE")
print("14. TO PRINT THE CURRENT POSITION OF THE TURTLE ")
print("15. TO PRINT THE CURRENT X-COORDINATE OF THE TURTLE")
print("16. TO PRINT THE CURRENT Y-COORDINATE OF THE TURTLE")
print("17. TO PRINT THE DIRECTION OF THE TURTLE HEAD")
print("18. TO PRINT THE TOTAL DISTANCE COVERED BY TURTLE")
print("BY DEFAULT PEN IS DOWN")
print("19. TO MAKE THE TURTLE PEN DOWN(NOT NOTICABLE, TILL PEN IS UP)")
print("20. TO MAKE THE TURTLE PEN UP(NOT NOTICABLE TILL PEN IS DOWN)")
print("21. TO PRINT THE WIDTH OF THE TURTLE LINE")
print("22. TO MAKE A CIRCLE OF A RADIUS(R)")
print("23. TO SHOW BOOLEAN WETHER THE PEN IS DOWN")
print("24. TO SHOW THE COLOR OF THE PEN ")
print("25. TO DELETE THE TURTLE DRAWINGS ON THE CANVAS ")
print("26. TO DELETE THE TURTLE DRAWINGS ON THE CANVAS BUT DO NOT MOVE THE TURTLE ")
print("27. TO WRITE THE TEXT ON THE CANVAS ")
print("28. TO HIDE THE TURTLE ON THE SCREEN(BETTER FOR COMPLEX DRAWINGS)")
print("29. TO SHOW THE TURTLE(NOTICBLE ONLY WHEN TURTLE IS HIDDEN ) ")
print("30. TO RETURN BOOLEAN FOR THE SHOW OF THE TURTLE")
print("31. TO TILT THE TURTLE THROUGH SOME SPECIFIC ANGLE")
print("32. TO SHOW THE ANGLE OF TILT OF THE TURTLE")
print("33. TO RETURN THE COORDINATES OF THE CURRENT POLYGON(WILL NOT WORK IF THE POLYGON IS NOT THERE)")
print("34. TO DISPLAY THE TOTAL DISTANCE COVERED BY TURTLE")
print("35. TO MAKE A CLONE OF THE CURRENT TURTLE ")
print("36. TO ADJUST THE SPEED OF TURTLE MOVEMENT ")
print("37. TO SHOW THE ATTRIBUTES OF ALL THE TURTLES ON THE CANVAS ")
print("38. TO SHOW THE HEIGHT OF THE CANVAS ")
print("39. TO SHOW THE WIDTH OF THE CANVAS ")
print("40. TO EXIT THR TURTLE ")
choice = int(input("Enter your choice : "))
if choice == 1:
    a = int(input("Enter the amount of distance : "))
    fd(a)
elif choice == 2:
    a = int(input("Enter the amount of distance : "))
    bk(a)
elif choice == 3:
    a = int(input("Enter the amount of degree : "))
    rt(a)
elif choice == 4:
    a = int(input("Enter the amount of degree : "))
    lt(a)
elif choice == 5:
    a = int(input("Enter the coordinate : "))
    goto(a)
elif choice == 6:
    a = int(input("Enter the coordinate of the x-axis : "))
    sx(a)
elif choice == 7:
    a = int(input("Enter the coordinate of the y-axis : "))
    sy(a)
elif choice == 8:
    he()
elif choice == 9:
    a = int(input("Enter the radius : "))
    circle(a)
elif choice == 10:
    a = int(input("Enter the thickness : "))
    dot(a)
elif choice == 11:
    stamp()
elif choice == 12:
    clearstamp()
elif choice == 13:
    a = int(input("Enter the amount of speed : "))
    speed(a)
elif choice == 14:
    pos()
elif choice == 15:
    xcor()
elif choice == 16:
    ycor()
elif choice == 17:
    heading()
elif choice == 18:
    dis()
elif choice == 19:
    pd()
elif choice == 20:
    pu()
elif choice == 21:
    a = int(input("Enter the width of the pen : "))
    width(a)
elif choice == 22:
    pen()
elif choice == 23:
    isd()
elif choice == 25:
    pro()
elif choice == 26:
    ret()
elif choice == 27:
    cr()
elif choice == 28:
    a = str(input("Enter the text : "))
    we(a)
elif choice == 29:
    hide()
elif choice == 30:
    se()
elif choice == 31:
    ie()
elif choice == 32:
    a = int(input("Enter the amount of titlness : "))
    tilt(a)
elif choice == 33:
    tilt()
elif choice == 34:
    get_shapepoly()
elif choice == 35:
    clone()
elif choice == 36:
    a = int(input("Enter the amount of delay : "))
    delay(a)
elif choice == 37:
    turtles()
elif choice == 38:
    window_height()
elif choice == 39:
    window_width()
elif choice == 40:
    bye()

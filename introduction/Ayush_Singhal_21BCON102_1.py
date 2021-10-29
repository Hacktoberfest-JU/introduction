#MY NAME IS AYUSH SINGHAL
#THIS CODE CONSISTS OF CALCULATING AREAS OF VAROUS SYMMETRIC SHAPES

#THE SIMPLEST - RECTANGLE
def rectangle(Lenght , Breadth):
    Area = (Length*Breadth)
    print(Area)
#THE MOST EFFICIENT - CIRCLE
def circle(Radius):
    Area = (Radius*Radius*3)
    print(Area)
#THE LOVE - TRIANGLE
def triangle(Base , Height):
    Area = (Height*Base)
    print(Area)

#THIS CODE CONSISTS OF MAKING SOME COMPLEX SHAPES

#THE EGYPTIANS - PYRAMID
def pyramid(n):
    for i in range(n):
        for j in range(i+1):
            print(j+1, end=" ")
        print()
#THIS AGAIN
def dimaryp(n):
    for i in range(n):
        for j in range(i, -1, -1):
            print(j+1, end=" ")
        print()
#NOT AGAIN
def pyyramid(n):
    for i in range(n):
        for j in range(i, -1, -1):
            print(i+1, end=" ")
        print()
#THIS CODE CONSISTS OF A SIMPLE COLLEGE MARKS MANAGMENT SYSTEM OF A PARTICULAR STUDENT

#LET THE MARK LIST IS
Marks = [98, 67, 89, 76, 65, 93, 82, 94]

#ADDITION OF MARKS
def add(Number):
    Marks.append(Number)
#ADDITION OF MARKS AT DESIRED POSITION
def addin(Number, Index):
    Marks.append(Number, Index)
#DELETION OF MARKS
def delete(Number):
    Marks.remove(Number)
#SORTING OF MARKS IN ASCENDING ORDER
def ascending():
    Marks.sort()
#SORTING OF LIST IN DESCENDING ORDER
def descending():
    Marks.sort(reverse = True )
print("1. Area of the Rectangle")
print("2. Area of the Circle")
print("3. Area of the Triangle")
print("4. Creating a Pyramid")
print("5. Creating a Pyramid in reverse order")
print("6. Creating a Pyramid in the same order")
print("College Marks Managment System tarts from here!!!")
print("The list of the marks of the student is ", Marks)
print("7. Add the marks of the students")
print("8. Add the marks of the students at a desired position")
print("9. Delete  the marks of the students")
print("10. Sort the list in ascending order")
print("11. Sort the list in descending order")
print("12. Exit the Program")
choice = int(input("Enter your choice (1-12) : "))
if choice == 1:
    Length = int(input("Enter the Length of the Rectangle : "))
    Breadth = int(input("Enter the Breadth of the Rectangle : "))
    rectangle(Length, Breadth)
elif choice == 2:
    Radius = int(input("Enter the Radius of the Circle : "))
    circle(Radius)
elif choice == 3:
    Base = int(input("Enter the Length of the Base : "))
    Height = int(input("Enter the Altitude of Triangle :"))
    triangle(Base, Height)
elif choice == 4:
    Number = int(input("Enter the number of Rows : "))
    pyramid(Number)
elif choice == 5:
    Number = int(input("Enter the number of Rows : "))
    dimaryp(Number)
elif choice == 6:
    Number = int(input("Enter the number of Rows : "))
    pyyramid(Number)
elif choice == 7:
    Number = int(input("Enter the Marks to be added in the List : "))
    if Number >= 100:
        print("Please enter a number below 100!! : ")
    else:
        add(Number)
elif choice == 8:
    Number = int(input("Enter the marks to add in the List : "))
    if Number >= 100 :
            print("Please enter a number below 100!!")
    else :
        Index = int(input("Please enter the position of Marks : "))
        addin(Number, Index)
elif choice == 9:
    Number = int(input("Enter the Marks to be deleted : "))
    if Number in Marks :
        print("The number is not found in the List")
    else :
        delete(Number)
elif choice == 10:
    ascending()
    print("The marks in ascending order is : ", Marks)        
elif choice == 11:
    descending()
    print("The marks in descending order is : ", Marks)
elif choice == 12:
    pass
else :
    print("Please enter a valid choice")
            
    
    
        










a = float(input("enter first number:"))
b = float(input("enter second number:"))
c = float(input("enter third number:"))
s = (a + b + c) / 2
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f' %area)

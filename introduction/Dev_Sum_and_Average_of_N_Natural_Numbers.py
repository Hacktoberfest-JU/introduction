# Python Program to find Sum and Average of N Natural Numbers
 
number = int(input("Please Enter any Number: "))
total = 0

for value in range(1, number + 1):
    total = total + value

average = total / number

print("The Sum of Natural Numbers from 1 to {0} =  {1}".format(number, total))
print("Average of Natural Numbers from 1 to {0} =  {1}".format(number, average))

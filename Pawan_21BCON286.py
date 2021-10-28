#Find the factorial of inputted number.
num=int(input('Enter the number: '))
factorial=1
if num<0:
    print('Negative numbers dont have factorials')
elif num==0:
    print('The factorial of zero is 1')
else:
    for i in range(1,num+1):
        factorial=factorial*i
        print('The factorial of',num,'is',factorial)

print('\n\n')
print('PLEASE,ENTER NUMBER GREATER THAN 5,')
n1=int(input('enter your number:'))

if n1>5: 
 print('\n')
 print("Enter your choise for,\n"
       "\n 1.multiply by 6,\n"
       "\n 2. division by 9,\n"
       "\n 3. square of the number")
 choice=int(input('enter your choice'))
 if choice==1:
     multiple=n1*6
     print("multiplication of the number is,",multiple)
 elif choice==2:
     div=n1/9
     print("the devision of the number =",div)
 elif choice==3:
     sq=n1**2
     print("the square of the given number is",sq)
 elif choice>3:
     print("please enter number only from the given choice")

else:
    print('read the instructions again,you are asked to enter number greater than 5!')
print("\n")
print('you programe ENDS \n'
      '\n THANKYOU FOR JOINING IN')
print('-------------------------------------------------------------------------------------')

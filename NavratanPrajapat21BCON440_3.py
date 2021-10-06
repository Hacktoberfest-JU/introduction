Binary = list(input("Enter a Binary code to convert into a Decimal code:- "))
x = 0
for i in range(len(Binary)):
    y = Binary.pop()
    if y!='1' and y!='0':
        print('Please Enter a Valid Binary Code.')
        break
    elif y == '1':
        x = x + pow(2, i)
print('The Decimal Code is:-', x)  

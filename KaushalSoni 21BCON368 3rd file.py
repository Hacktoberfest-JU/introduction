# this program  is used to find number of employees of age group of 26 to 35 / 36 to 45 / 46 to 55 (please enter the integer value for age)
n=int(input('Total Number of Employees :'))
A='26 to 35'
B='36 to 45'
C='46 to 55'
ctA=0
ctB=0
ctC=0
for i in range(n,0,-1):
    L=float(input('Enter the age of the employee:'))
    if L<26:
        m='Please enter age between 26 and 55'
        print(m)
    elif 26<=L<=35:
        ctA +=1
    elif 36<=L<=45:
        ctB +=1
    elif 46<=L<=55:
        ctC +=1
print('Employees in age group ({0:5s}):{1:5d}'.format(A,ctA))
print('Employees in age group ({0:5s}):{1:5d}'.format(B,ctB))
print('Employees in age group ({0:5s}):{1:5d}'.format(C,ctC))

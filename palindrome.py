'''Write a Python program to check whether a given number is palindrome or not?'''
number = input()
if str(number)==str(number[::-1]):
print(f'{number} is palindrome number')
else:
print(f'{number} is not palindrome')

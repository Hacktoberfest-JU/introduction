print('Hello! My name is Jarvis.')
print('I was created in 2021.')
print('Please, remind me your name.')
name = input('Your Name : ')
print('What a great name you have, ' + name + '!')

print('Let me guess your age.')
print('Enter remainders of dividing your age by 3, 5 and 7.')
rem3 = int(input('Remainder by 3 : '))
rem5 = int(input('Remainder by 5 : '))
rem7 = int(input('Remainder by 7 : '))
age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105
print("Your age is " + str(age) + "; now you know that I am brilliant!")

print('Now I will show you that I can count to any number you want.')
count_till = int(input('Count till : '))
for x in range(1, count_till + 1):
    print(x, '!')
print('Completed!')

print("Let's test your programming knowledge.")
print("Which of the following contain a bool value?")
option_1 = "1. len()"
option_2 = "2. str.startswith()"
option_3 = "3. type()"
option_4 = "4. str.index()"
print(option_1)
print(option_2)
print(option_3)
print(option_4)
user_input = int(input('Type your option number : '))
while True:
    if user_input == 1 or user_input == 3 or user_input == 4:
        print('Incorrect. Please, try again.')
        user_input = int(input('Type your option number : '))
    elif user_input == 2:
        print("Awesome! it's correct.")
        break
    else:
        print("Please enter a number from 1 to 4 !")
        user_input = int(input('Type your option number : '))
print('Congratulations, have a nice day!')

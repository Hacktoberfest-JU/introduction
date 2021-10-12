income = int(input('Income : '))
global percent
if income >= 132407:
    percent = 28
elif income >= 42708:
    percent = 25
elif income >= 15528:
    percent = 15
elif income >= 0:
    percent = 0
calculated_tax = (percent * income) / 100
print(f'The tax for {income} is {percent}%. That is{calculated_tax : .0f} dollars!')

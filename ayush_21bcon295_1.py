water = 400
milk = 540
coffee_beans = 120
disposable_cups = 9
money = 550


def total_supplies():
    print(f'''The coffee machine has:
    {water} ml of water
    {milk} ml of milk
    {coffee_beans} g of coffee beans
    {disposable_cups} of disposable cups
    ${money} of money''')


while True:
    action = input('Write action (buy, fill, take, remaining, exit) : ')
    if action == 'buy':
        coffee_type = input('What do you want to buy? (1 - espresso, 2 - latte, 3 - cappuccino, back) : ')
        if coffee_type == '1':
            if water < 250:
                print('Sorry, not enough water!')
            elif coffee_beans < 16:
                print('Sorry, not enough coffee beans!')
            elif disposable_cups < 1:
                print('Sorry, not enough disposable cups!')
            else:
                print("I have enough resources, making you a coffee!")
                water -= 250
                coffee_beans -= 16
                disposable_cups -= 1
                money += 4
        elif coffee_type == '2':
            if water < 350:
                print('Sorry, not enough water!')
            elif milk < 75:
                print('Sorry, not enough milk!')
            elif coffee_beans < 20:
                print('Sorry, not enough coffee beans!')
            elif disposable_cups < 1:
                print('Sorry, not enough disposable cups!')
            else:
                print("I have enough resources, making you a coffee!")
                water -= 350
                milk -= 75
                coffee_beans -= 20
                disposable_cups -= 1
                money += 7
        elif coffee_type == '3':
            if water < 200:
                print('Sorry, not enough water!')
            elif milk < 100:
                print('Sorry, not enough milk!')
            elif coffee_beans < 12:
                print('Sorry, not enough coffee beans!')
            elif disposable_cups < 1:
                print('Sorry, not enough disposable cups!')
            else:
                print("I have enough resources, making you a coffee!")
                water -= 200
                milk -= 100
                coffee_beans -= 12
                disposable_cups -= 1
                money += 6
        elif coffee_type == 'back':
            continue
    elif action == 'fill':
        fill_water = int(input('Write how many ml of water you want to add : '))
        fill_milk = int(input('Write how many ml of milk you want to add : '))
        fill_coffee_beans = int(input('Write how many grams of coffee beans you want to add : '))
        fill_disposable_cups = int(input('Write how many disposable coffee cups you want to add : '))
        water += fill_water
        milk += fill_milk
        coffee_beans += fill_coffee_beans
        disposable_cups += fill_disposable_cups
    elif action == 'take':
        print(f'I gave you ${money}')
        money = 0
    elif action == 'remaining':
        total_supplies()
    elif action == 'exit':
        break
        

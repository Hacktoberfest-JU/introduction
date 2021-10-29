def sumofoddnumbers():
    l1 = []
    a = 'y'
    s = 0
    while a == 'y':
        n = int(input("Enter a number : "))
        l1.append(n)
        a = input("Enter more? (y/n): ")
    for i in l1:
        if i % 2 != 0:
            s = s + i
    print("Sum of odd numbers : ", s)

sumofoddnumbers()

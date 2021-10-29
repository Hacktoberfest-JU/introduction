def miniumvalue():
    l = []
    a = 'y'
    while a == 'y':
        n = int(input("Enter a number : "))
        l.append(n)
        a = input("Enter more? (y/n): ")
    m = min(l)
    print('Minimum value : ', m)


miniumvalue()

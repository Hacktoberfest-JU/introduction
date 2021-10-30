def mean():
    import statistics
    l1 = []
    a = 'y'
    while a == 'y':
        n = int(input("Enter a number : "))
        l1.append(n)
        a = input("Enter more? (y/n): ")
    m = statistics.mean(l1)
    print("Mean of numbers : ", m)

mean()

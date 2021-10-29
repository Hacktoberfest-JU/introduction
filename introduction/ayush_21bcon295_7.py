print('Give me a range of numbers and I will give you all prime numbers from it !')
starting = int(input('Starting Number : '))
ending = int(input('Ending Number : '))


def prime(n):
    if n == 1:
        return False
    for d in range(2, n):
        if n % d == 0:
            return False
    else:
        return True


for n in range(starting, ending + 1):
    print(n, prime(n))

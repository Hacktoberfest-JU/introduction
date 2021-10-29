n=int(input("Up to which NATURAL NUMBER : "))
a=1
sum_even=sum_odd=0
while a<=n:
    if a%2==0:
        sum_even+=a
    else:
        sum_odd+=a
    a+=1
print("The sum of even integers is ",sum_even)
print("The sum of odd integers is ",sum_odd)

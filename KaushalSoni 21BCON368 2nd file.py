# program to calculate total fund raised by Charity Camp
TA = 0
count =1
while count <=3:
    CS=float(input('Charity Sales Amount on Day'+str(count)+':'))
    TA += CS
    D=float(input('Donation Amount on Day'+str(count)+':'))
    TA += D
    count += 1
if TA >= 200000:
    More=TA-200000
    print('Charity Camp Successfully raised Rs.',More,'more than Rs. 200000')
else:
    Less = 200000 - TA
    print('We are Short of Rs.',Less,'from the intended Amount of RS. 200000')

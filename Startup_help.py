Idea_1 = 'This is Your Idea_1. PS idea is confidential.'
Idea_2 = 'This is Your Idea_2. PS idea is confidential.'

print(Idea_1)
print(Idea_2)

mrSur_Ch1 = 73/100
mrSur_Ch2 = 75/100

invst1 = 1000000
invst2 = 2000000

lngTrm_sprt1 = 5 # in years
lngTrm_sprt2 = 6 # in years

print('The Idea_1 has ' + str(mrSur_Ch1) + ' chances to srvive in market')
print('The Idea_2 has ' + str(mrSur_Ch2) + ' chances to srvive in market')

if mrSur_Ch1 >= 75/100 and invst1 >= 1000000 and lngTrm_sprt1 >= 5 :
    print('You may go with Idea_1.')
if mrSur_Ch2 >= 75/100 and invst2 >= 1000000 and lngTrm_sprt2 >= 5:
    print('You may go with Idea_2.')

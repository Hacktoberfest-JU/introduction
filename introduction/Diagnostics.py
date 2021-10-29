Diagnosis = ['Blood Test', 'CT Scan', 'MRI']
x = input('Which Test would you like to have? : ')
if x == Diagnosis[0]: 
    print('Go to Lab no. 1')
elif x == Diagnosis[1]:
    print('Go to Lab no. 2')
elif x == Diagnosis[2]:
    print('go to Lab no. 3')   
else:
    print('Please Enter Correct Information OR May be this Test is NOT AVAILABLE here.')

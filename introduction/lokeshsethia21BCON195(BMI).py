print("\t\tWelcome To Body Mass Index Calculator")
Weight=int(input("Please Enter Your Weight(in kg):- "))
Height=float(input("Please Enter Your Height(in feet):- "))
H1=Height/3.28
BMI=Weight/(H1**2)
print("Your Body Mass Index is",BMI)
if BMI<=18.5:
    print("You Are Undernourished, Kindly have some Healthy Diet☻☻")
elif 18.5<=BMI and BMI<25:
    print("You Are a Healthy Person, You Are Going to Live Long☻☻")
elif 25<=BMI and BMI<30:
    print("You Are a Overweight, You have to Work Hard to Maintain Yourself☻☻")
elif 30<=BMI and BMI<35:
    print("You Are in Obesity Class I, Go to Gym☻☻")
elif 35<=BMI and BMI<40:
    print("You Are in Obesity Class II, Go to Gym and Also Take Proper Diet☻☻")
else:
    print("You Are in Obesity Class III, Go to Gym, Work Hard and Also Take Proper Diet☻☻")

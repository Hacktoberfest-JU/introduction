#BMI Calculator

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in cm: "))
BMI = weight / (height/100)**2

if BMI<18.5:

   print("Underweight")

elif (BMI >= 18.5) and (BMI < 25):

   print("Normal")

elif (BMI >= 25) and (BMI < 30):

   print("Overweight")

else:

   print("Obesity")

print("What is your name human?")
name = input()
print()
print("How old are you (in years)?")
userage = int(input())
print()
print("How tall are you (in meters)?")
height = float(input())
print()
print("How much do you weigh (in kilograms)?")
weight = int(input())
print()
BMI = weight / (height * height)
print(name + " you are " + str(userage) + " years old and your bmi is " + str(round(BMI,2)))
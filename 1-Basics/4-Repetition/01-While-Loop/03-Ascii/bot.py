charge = 0
bars= int(input("How many bars should be charged?: "))

while (charge <= bars):
    print("Charging:" + "█ " * charge)
    charge = charge + 1
print("The battery is fully charged.")


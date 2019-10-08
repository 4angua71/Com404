tentries = 1
total = 0
entries = int(input("How many numbers should I sum up?: "))

while (tentries <= entries):
    centries = int(input("Please enter number " +str(tentries)+ " of " + str(entries)+ " : "))
    tentries = tentries +1
    total = total + centries

print("The answer is " + str(total))
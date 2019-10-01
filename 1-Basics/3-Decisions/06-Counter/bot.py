Even_count = 0
Odd_count = 0

first = int(input("Please enter the first number: "))
second = int(input("Please enter the second number: "))
third = int(input("Please enter the third number: "))

if(first % 2 == 0):
     Even_count = Even_count + 1
else:
    Odd_count = Odd_count + 1
if(second % 2 == 0):
     Even_count = Even_count + 1
else:
    Odd_count = Odd_count + 1
if(third % 2 == 0):
     Even_count = Even_count + 1
else:
    Odd_count = Odd_count + 1

print("There were ", Even_count, "even and " , Odd_count, "odd numbers" )
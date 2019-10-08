N  = int(input("What level of brightness is required?: "))


print("Adjusting brightness...")
for count in range(2, N+1, 2):
    print()
    print("Beep's brightness level: " + "*" * count)
    print("Bop's brightness level: " + "*" * count)
    
print()
print("Adjustments complete!")


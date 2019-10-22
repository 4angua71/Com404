health = 100

print("Your health is ",health, "%. Escape is in progress...")

for count in range(0, 5, 1):
        response = str(input("…Oh dear, who is that?"))
        if(response == "Smiler's Bot"):
            print("Time to jam out of here!")
            health = health -20
        elif(response == "Hacker"):
            print("Yay! Better follow this one!")
            health = health +20
        else:
            print("Phew, just another emoji!","|", end="")
print("Escaped! Health is ", str(health), "%")


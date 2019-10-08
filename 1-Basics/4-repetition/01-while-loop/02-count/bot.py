detatchments = 0
cables = int(input("How many live cables must I avoid?: "))

while (detatchments < cables):
    print("Avoiding......Done! " + str(detatchments+1) + " live cable avoided!")
    detatchments = detatchments + 1
print("All live cables have been avoided.")
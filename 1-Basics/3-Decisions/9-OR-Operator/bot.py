type = str(input("Please enter adventure type (scary/safe/short/long/mystery): "))
if (type == "scary") or (type == "short"):
    print("Entering the dark forest!")
elif (type == "safe") or (type == "long"):
    print("Taking the safe route!")
else:
    print("Not sure which route to take.")



location = str(input("Where should i look?: "))
if (location == "in the bedroom"):
    areaa = str(input("Where in the bedroom should I look?: "))
    if (areaa == "under the bed"):
        print("Found some shoes but no battery")
    else:
        print("Found some mess but no battery")
elif (location == "in the bathroom"):
    areab = str(input("Where in the bathroom should I look?: "))
    if (areab == "in the bathtub"):
        print("Found a rubber duck but no batter")
    else:
        print("It is wet but I found no battery")
elif (location == "in the lab"):
    areac = str(input("Where in the lab should I look?: "))
    if (areac == "on the table"):
        print("Yes! I found my battery")
    else:
        print("Found some tools but no battery.")
else:
    print("I do not know where that is but I will keep looking")


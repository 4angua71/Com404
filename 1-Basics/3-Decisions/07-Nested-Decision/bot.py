cover = str(input("Please Enter Book Cover Type (Soft/Hard) : "))
if (cover == "Soft"):
    cbound = str(input("Is the book perfect bound?(Yes/No): "))
    if (cbound == "Yes"):
        print("Soft cover, perfect bound books are very popular!")
    else:
        print("Soft covers with coils or stitches are great for short books")
else:
    print("Books with hard covers can be more expensive!")

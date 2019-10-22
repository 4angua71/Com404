# 1st Function
def is_league_united(hero1, hero2):
    if(hero1 == "Superman" or "Wonder Woman") and (hero2 == "Superman" or "Wonder Woman"):
        return True

    else:
        return False

# 2nd Function
def decide_plan(hero1, hero2): 
    if is_league_united(hero1, hero2) == True:
        print("Time to save the world!")
    elif is_league_united(hero1, hero2) == False:
        print("We must unite the league!")
    else:
        print("why isn't this working?!?!!?")

# 3rd Function
def run(): 
    hero1 = str(input("Enter name of first hero: "))
    hero2 = str(input("Enter name of second hero: "))
    prompt = str(input("league or plan?: "))
    if(prompt == "league"):
        is_league_united(hero1, hero2)
    elif(prompt == "plan"):
        decide_plan(hero1, hero2)
    else:
        print("Invalid command. Please try again")

# Run the program
run()
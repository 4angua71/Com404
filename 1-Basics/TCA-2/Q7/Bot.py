#from functions import 1,2,3,4

# Option 1
def Option_1 (phrase,count): 
    while (count < len(phrase)):
            print("*",end="")
            count = count+ 1
    print()
    print(phrase)

# Option 2
def Option_2 (phrase,count): 
    print(phrase)
    while (count < len(phrase)):
        print("*",end="")
        count = count+ 1

# Option 3
def Option_3 (phrase,count):
    while (count < len(phrase)):
        print("*",end="")
        count = count+ 1
    print()
    print(phrase)
    while (count < len(phrase)):
        print("*",end="")
        count = count+ 1



phrase= str(input("Please enter a phrase: "))
option = int(input("Please enter option required (1-4)"))
count = 0

if(option == 1):
    Option_1(phrase,count)
elif(option == 2):
    Option_2(phrase,count)
elif(option == 3):
    Option_3(phrase,count)




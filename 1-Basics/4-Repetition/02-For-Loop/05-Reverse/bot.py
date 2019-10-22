
user_word = str(input("What phrase do you see?"))

print("Reversing...\n")
print("The Phrase is: ",end="")
for position in range(len(user_word)-1, -1, -1):
    print(user_word[position],end="")
print()
user_word = str(input("What phrase do you see?"))
answer = ""

print("Reversing...\n")
for word in user_word:
    answer = word + answer
print("The Phrase is: " + answer)


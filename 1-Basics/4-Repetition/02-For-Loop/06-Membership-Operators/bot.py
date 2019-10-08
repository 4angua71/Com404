user_word = str(input("What phrase do you see?"))
answer = ""

print("Reversing...\n")
for word in user_word:
    answer = word + answer
print("The Phrase is: " + answer)

#phrase = "hello"

#answer = ""
#for meh in phrase:
 #   answer = meh + answer
##
#print(answer)
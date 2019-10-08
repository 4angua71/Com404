
user_word = input("What strange markings do you see?")

print("Identifying...\n")
for position in range(0, len(user_word), 1):
    print("index " + str(position)+ ":" + user_word[position])
print("\nDone!")
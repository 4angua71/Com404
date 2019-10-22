sequence = input("Please enter a sequence:")
marker = input("Please enter the characterfor the marker:")

marker1_position = -1
marker2_position = -1

for position in range(0, len(sequence), 1):
    letter = sequence[position]

    if (letter == marker):
        if (marker1_position == -1):
            marker1_position = position
        else:
            marker2_position = position

print("The distance between the markers is", marker2_position - marker1_position - 1)
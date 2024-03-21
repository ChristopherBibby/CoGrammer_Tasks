# Save a user's sentence as a string

str_manip = input("Please enter a sentence ")

# Calculate and print the length of the string

print(len(str_manip))

# Find the last letter in the sentence and replace every occurance of it with @ using the x function

edit = str_manip.replace(str_manip[-1], "@")

# print the edited sentence

print(edit)

# select the final 3 letters of the sentence

ending = str_manip[-3] + str_manip[-2] + str_manip[-1]

# reverse and print these the letters

print(ending[::-1])

# select the first three letters of the sentence and the last two letters of the sentence

start = str_manip[0] + str_manip[1] + str_manip[2]
end = str_manip[-2] + str_manip[-1]

# combine the two selected letter groups together

merge = start + end

# print out the combined letter selections

print(merge)
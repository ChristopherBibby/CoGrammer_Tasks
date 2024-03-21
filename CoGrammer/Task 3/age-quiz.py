# Input command to request user's age

age = int(input("Please enter your age: "))

# if-elif-else statements to catogorise age groups
# The code to print out the revelent message for the entered age group

if age < 13:
    print("You qualify for the kiddie discount.")

elif age == 21:
    print("Congrats on your 21st!")

elif age < 40:
    print("Age is but a number.")

elif age < 65:
    print("You're over the hill!")

elif age < 100:
    print("Enjoy your retirement!")

else:
    print("Sorry, you're dead.")
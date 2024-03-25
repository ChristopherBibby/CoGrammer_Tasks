# define variable for the time of each event
# then calculate the total time for the triathlon

while True:
    try:
        swim = int(input("Please enter the time for the swimming event in minutes: "))
        cycle = int(input("Please enter the time for the cycling event in minutes: "))
        run = int(input("Please enter the time for the running event in minutes: "))
        break  # Break out of the loop if all inputs are successfully converted to integers
    except ValueError:
        print("Please enter numeric values only.")

total = swim + cycle + run

# if-elif-else statements to determine the award recieved for the imputed time
# then a print of a relevent message for the award acheived

if total <= 100:
    print(f"Congratulations time of {total} minutes qualified for the Provincal Colours!")

elif total <= 105:
    print(f"Congratulations time of {total} minutes qualified for the Provincal Half Colours!")

elif total <= 110:
    print(f"Congratulations time of {total} minutes qualified for the Provincal Scroll!")

else:
    print(f"Unforunately your time of {total} minutes did not qualify you for an award.")
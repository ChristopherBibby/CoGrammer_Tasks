# enter a variables to keep track of the values entered and values needed for calculations

num1 = 0
total = 0
num_entered = 0

#  request the user to enter a number
#  use while code to end the requests for user input when -1 is entered
#  then enter code to calculate the average of the entered values and display them to the user

while True:
    num1 = float(input("Please enter a number: "))
    if num1 == -1:
        break
    total += num1
    num_entered += 1

# Avoid division by zero if no numbers entered
average = total / num_entered if num_entered > 0 else 0 
print(f"Your average number input was {average}!")
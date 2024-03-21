# use an input function to request  3 seperate integers

num1 = int(input("Please enter an integer: "))
num2 = int(input("Please enter another integer: "))
num3 = int(input("Please enter one more integer: "))

# Calculate and print he sum of the integers

total = int(num1 + num2 + num3)
print(total)

# Calculate and print the first number minus the second number

total2 = int(num1 - num2)
print(total2)

# Calculate and print the third number multiplied by the first number

total3 = int(num3 * num1)
print(total3)

# Calculate and print the sum of all three numbers divided by the third number

total4 = int(num3 * (num1 + num2 + num3))
print(total4)
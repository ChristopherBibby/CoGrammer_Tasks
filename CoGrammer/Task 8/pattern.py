# Set the number of rows for the pattern
rows = 5

# Loop to iterate through each row
for x in range(1, rows * 2):

# Calculate the number of asterisks to print in each row
    if x <= rows:
        num_asterisks = x
    else:
        num_asterisks = 2 * rows - x

# Loop to print '*' in each column
    for y in range(num_asterisks):
        print("*", end=" ")
        

# Move to the next line after each row
    print()
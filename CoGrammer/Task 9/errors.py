# This example program is meant to demonstrate errors.

# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

# Syntax error = incorrect placement of /n and lack of brackects

print ("Welcome to the error program"), '/n'


# Syntax error = incorrect indentation and use of '==' instead of '=' for defining a variable 
# Logic Error = wrong variable (int instead of str) used for printing
# Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24 years old" 
age = 24 
print("I'm " + age_Str + " years old.")

# Syntax error = incorrect indentation
# Runtime error = 'years_from_now' should be an integer not a string
# Variables declaring additional years and printing the total years of age
years_from_now = int("3")
total_years = age + years_from_now

# Logic error = total_years needed to be cast to a string
answer_years = str(total_years)

# Syntax error = lack of brackects
print ("The total number of years: " + answer_years)

# Syntax error = lack of brackects and  wro6ng variable used ('total' instead of 'total_years')
# Logic error = the extra 6 months were no included in the total months variable
# Variable to calculate the total amount of months from the total amount of years and printing the result
int_total_months = (total_years * 12) + 6
total_months = str(int_total_months)
print ("In 3 years and 6 months, I'll be " + total_months + " months old")

#HINT, 330 months is the correct answer


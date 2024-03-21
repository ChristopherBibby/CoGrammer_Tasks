import math

# print out the definitions for both bond and investment
# user inputs whether they want either an investment or bond

print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond     - to calculate the amount you'll have to pay on a home loan")

type = input("Enter either 'invesment' or 'bond' from the menu above to proceed: ")

new_type = type.lower()

# Code for if investment is entered
# request revelvant inputs for calcualting the formula determining their investment value
# then calculate and print the determined value

if new_type == "investment":
   amount = int(input("Please enter the amount of money you are depositing: "))
   rate = int(input("Please enter your interest rate (please do not enter the percentage symbol): "))
   years = int(input("Plaese enter the number of years you plan on investing: "))
   interest0 = input("Enter either 'simple' or 'compound' depending on which you would prefer: ")
   
   interest1 = interest0.lower()

   if interest1 == "simple":
    Total1 = int(amount * (1 + ((rate/100) * years)))
    print(f"The value of your investment will be £{Total1} after {years} years")

   if interest1 == "compound":
    Total2 = int(amount * (1 + ((rate/100))** years))
    print(f"The value of your investment will be £{Total2} after {years} years")

# Code for if bond is entered
# request the relevant inputs for calculating the formule to determine the cost their bond repayments
# then calcutae and print the determined value

if new_type == "bond":
  house = int(input("Please enter the value of the house: "))
  rate2 = int(input("Please enter the interest rate for the loan (please do not enter the percentage symbol): "))
  months = int(input("Please enter the number of months over which the bond will be repaid: "))

  total3 = int((rate2/12)*house)/(1-(1+(rate2/12))**(-months))
  print(f"Your monthly repayments will be £{total3} per month" )
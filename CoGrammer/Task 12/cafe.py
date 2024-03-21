# Define the menu
menu = {
    'coffee': 5,
    'tea': 3,
    'sandwich': 8,
    'cake': 6
}

# Define the stock of each item in the menu
stock = {
    'coffee': 100,
    'tea': 50,
    'sandwich': 30,
    'cake': 20
}

# Calculate the total stock worth
total_stock_worth = sum(stock[item] * menu[item] for item in menu)

# Print the results
print("Menu:")
for item, price in menu.items():
    print(f"{item.capitalize()}: ${price}")

print("\nStock:")
for item, quantity in stock.items():
    print(f"{item.capitalize()}: {quantity}")

print("\nTotal Stock Worth: $" + str(total_stock_worth))
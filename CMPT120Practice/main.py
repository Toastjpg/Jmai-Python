#########################################
#
# Title: Shopping list calculator
# Author Name: Johnny Mai
# Date: 2020-10-05
# Description: Asks user for the price of each item and returns the total, applies discount for certain prices
#
#########################################

cartList = ["cabbage", "bread", "milk", "eggs"]
priceList = []
cartTotal = 0

# Asks user price of each item in list
for i in cartList:
    priceInput = float(input(f"What is the price of {i}?\n>>> ").strip("$"))
    priceList.append(priceInput)

# Accumulates the inputted price in priceList
for i in priceList:
    cartTotal += i

# Returns list of items, individual prices, and cart total with any taxes and discounts applied
print("Item: \t\t Price:")
for i in range(len(cartList)):
    print(f"{cartList[i]}\t\t${priceList[i]:.{2}f}")
print(f"\nTotal:\t${cartTotal:.{2}f}")

# Applies 5% discount if total is over $10.00
if cartTotal >= 10.00:
    print(f"\nYour cart total is over $10.00! A 5% discount will be applied.")
    cartTotal = cartTotal * 0.95
    print(f"Discounted Total:\t${cartTotal:.{2}f}")



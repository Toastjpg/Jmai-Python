price = 0.0

burger = input("Would you like burger for $5? (Yes/No)\n>>> ").lower()
fries = input("Would you like fries for $3? (Yes/No)\n>>> ").lower()

if burger == "yes":
    price += 5
if fries == "yes":
    price += 3

total = price * 1.14
print(f"Your total is ${total:.2f}.")

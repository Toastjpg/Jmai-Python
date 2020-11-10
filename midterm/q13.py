menu = ["Sandwich $5", "Salad $4", "Juice $2", "Apple $1"]
price_List = [5, 4, 2, 1]

print("Lunch Menu")
for item in menu:
    print(item)

user_Input = input("Enter a comma separated list of quantities: ").split(",")

total = 0
for i in range(len(user_Input)):
    total += int(user_Input[i]) * price_List[i]

print(f"Total for your lunch is ${total}")

score = 0.0

for i in range(1, 6, 1):
    judge = int(input(f"Judge {i}: "))
    if 0 <= judge <= 10:
        score += judge
    else:
        print("Invalid Input")

print(f"Your olympic score is {score / 5}")

print("Please enter hobbies separated by spaces:")
p1 = input("Person 1: ").lower()
p2 = input("Person 2: ").lower()
similar = 0

for i in p1.split(" "):
    if i in p2.split(" "):
        similar += 1

print(f"You have {str(similar)} hobbies in common!")
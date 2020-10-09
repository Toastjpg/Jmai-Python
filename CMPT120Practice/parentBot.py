questions = ["Did you eat?", "Did you study?", "Did you do laundry?", "Did you call grandma?"]
count = 0

for i in questions:
    print(i)
    response = input(">>> ").lower()
    if response == "yes":
        count +=1

if 3 <= count <= 4:
    print("Good!")
elif 1 <= count <= 2:
    print("Ok.")
elif count == 0:
    print("Im coming over. ")
else:
    print("???")
def load_file():
    file = open("auto_safety.csv")
    rows = file.readlines()[1:]
    temp = []

    for line in rows:
        line = line.strip().split(",")
        temp.append(line)
    return temp


def binary_search_score(list, num):
    first = 0
    last = len(list) - 1
    found = False

    while first <= last and not found:
        mid = (first + last)//2
        if list[mid][0] == str(num):
            found = True
        else:
            if num > int(list[mid][0]):
                last = mid - 1
            else:
                first = mid + 1
    if found:
        return mid
    else:
        return -1


def selection_sort(list):
    for i in range(len(list)):
        min = int(list[i][-1])
        min_index = i

        for j in range(i + 1, len(list)):
            if int(list[j][-1]) < min:
                min = int(list[j][-1])
                min_index = j
        list[min_index], list[i] = list[i], list[min_index]
    return list


data = load_file()
userInput = int(input("What is the minimum safety ranking? "))
list = []

while userInput <= 30:
    index = binary_search_score(data, userInput)
    list.append(data[index])
    userInput += 1

sortData = selection_sort(data)
sortList = selection_sort(list)

print("Here are the cars with your minimum safety ranking, sorted by price:")
print(sortList)

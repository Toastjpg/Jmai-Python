records = open("sales_records.csv", "r")

count = 0
for line in records:
    row = line.split(",")
    if row[2].strip() == "Household":
        count += int(row[8].strip())

print(count)
records.close()

#
# Week 5 coding assignment q4.py
# Author: Johnny Mai
# Date: October 14, 2020
#
# q4.py - How many people rated movie 90? 

file = open("movies-wk5-ratings.csv")
count = 0

for line in file:
    movie90 = line.split(",")[92]
    if -10 <= float(movie90) <= 10:
        count += 1

print(f"Number of people who rated movie 90: {count}")

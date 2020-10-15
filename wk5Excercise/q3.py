#
# Week 5 coding assignment q3.py
# Author: Johnny Mai
# Date: October 14, 2020
#
# q3.py - How many people rated just 1 movie?
#         How many people rated >100 movies? 

file = open("movies-wk5-ratings.csv")
oneCount = 0
hundredCount = 0

for line in file:
    ratings = int(line.split(",")[1])
    if ratings == 1:
        oneCount += 1
    elif ratings >= 100:
        hundredCount += 1

print(f"Number of people who rated 1 movie: {oneCount}")
print(f"Number of people who rated >100 movies: {hundredCount}")

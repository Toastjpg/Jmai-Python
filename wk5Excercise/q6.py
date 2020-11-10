#
# Week 5 coding assignment q6.py
# Author: Johnny Mai
# Date: October 14, 2020
#
# q6.py - Ask the user for a rater ID between 1 to 7669,
#         then print all the movies ratings for that rater (not including 99).
#         Assume that the user types a correct ID.
#         Each movie rating should be printed on a separate line. 

file = open("movies-wk5-ratings.csv")
userInput = int(input(">>> "))

for line in file:
    raterID = int(line.split(",")[0])
    ratings = line.split(",")[2:]
    if userInput == raterID:
        print(f"Rater ID: {raterID}")
        for i in range(len(ratings)):
            if (-10 <= float(ratings[i]) <= 10) and (float(ratings[i] != 99)):
                print(ratings[i])

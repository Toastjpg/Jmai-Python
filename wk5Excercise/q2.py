#
# Week 5 coding assignment q2.py
# Author: Johnny Mai
# Date: October 14, 2020
#
# q2.py - What is the total number of ratings submitted over all raters?
#         What's the average number of movies rated by a person?
#
#         Important: From the previous question we know there are 7669 
#         raters in movies-wk5-ratings.csv. *Don't* use that number 
#         explicitly (hard coded) anywhere in your program! Your program 
#         should work for any number of raters (greater than 0), 
#         i.e. if the file had a different number of raters.

ratings = open("movies-wk5-ratings.csv", "r")
ratingsCount = 0
raters = []

for line in ratings:
    person = line.split(",")[0]
    ratings = line.split(",")[2:]
    for number in ratings:
        if (-10 <= float(number) <= 10) and (float(number) != 99):
            ratingsCount += 1
    raters.append(person)
print(f"Number of total ratings submitted: {ratingsCount}")

avgRate = ratingsCount//len(raters)

print(f"There are {len(raters)} raters, and {ratingsCount} ratings, with an average number of ratings per person being {avgRate}")
#
# Week 5 coding assignment q5.py
# Author: Johnny Mai
# Date: October 14, 2020
#
# q5.py - Ask the user for a movie ID between 1 to 158,
#         then print that movie title (just the movie title, not its ID).
#         Assume that the user types a correct ID. 

movies = open("movies-wk5.csv")
rows = movies.readlines()[1:]
userInput = int(input(">>> "))

for line in rows:
    id = line.split(",")[0]
    name = line.split(",")[1]
    if userInput == int(id):
        print(name)

movies.close()
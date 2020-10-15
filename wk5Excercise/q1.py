#
# Week 5 coding assignment q1.py
# Author: Johnny Mai
# Date: October 14, 2020
#
# q1.py - How many movies are in movies-wk5.csv?
#         How many raters are in movies-wk5-ratings.csv?

movies = open("movies-wk5.csv", "r")
movieRows = movies.readlines()[1:]
print(f"The number of movies in movies-wk5.csv is {len(movieRows)}.")
movies.close()

ratings = open("movies-wk5-ratings.csv", "r")
ratingRows = ratings.readlines()
print(f"The number of raters in movies-wk5-ratings.csv is {len(ratingRows)}.")
ratings.close()

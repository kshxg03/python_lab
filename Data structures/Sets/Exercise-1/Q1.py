

#Ask user for movies released in year 2025 and store as set. Ask user again for movies watched (any year) and perform following
# Find movies released in 2025 that user has watched
# Find movies released in 2025 that user has not watched
# Find movies watched by user that were not released in 2025


movies_2025 = set(input("Enter movies released in 2025 (seperate with space): ").split(" "))
# print(movies_2025)

movies_watched = set(input("Enter movies watched in any year (seperate with space): ").split(" "))

movies_user_watched_2025 = movies_2025 & movies_watched
print(movies_user_watched_2025)

movies_user_not_watched_2025 = movies_2025 - movies_watched
print(movies_user_not_watched_2025)

movies_user_watched_not_2025 = movies_watched - movies_2025
print(movies_user_watched_not_2025)

# any year, case where movies watched in other year can contain 2025 released movie


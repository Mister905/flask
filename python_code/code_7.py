# Booleans

print(5 == 5)

print(5 > 5)

print(5 != 5)


# if statement

day_of_week = input("What days is it today?\n")

if day_of_week == "Monday":
    print("Have a great Monday")
elif day_of_week == "Tuesday":
    print("Have a great Tuesday")
else:
    print("Have a great day")


# "in" keyword

movies_watched = { "The Matrix", "The Godfather", "Platoon" }

user_movie = input("What movie did you watch?\n")

print(user_movie in movies_watched)

if user_movie in movies_watched:
    print(f"I've watched {user_movie} too!")
else:
    print("I haven't seen that")
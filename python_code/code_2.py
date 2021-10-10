from datetime import date

name = "James"

greeting = f"Hello, {name}"

print(greeting)

# python3 code_2.py 
# Hello, James


# Alternatively

# name = "James"

# greeting = "Hello, {}"

# greeting_with_name = greeting.format(name)

# print(greeting_with_name)

longer_phrase = "Hell, {}. Today is {}"

today = date.today()

formatted = longer_phrase.format("James", today)

print(formatted)
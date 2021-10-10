# Dictionaries

friend_ages = { "James": 30 }

print(friend_ages["James"])

friends = [
    {"name": "Tim", "age": 25},
    {"name": "Joe", "age": 32},
    {"name": "Tina", "age": 18},
]

print(friends[2]["age"])

print(friends[0]["name"])

friend_dict = { "Tim": 25, "Joe": 32, "Tina": 18 }

for friend in friend_dict:
  print(f"{friend}: {friend_dict[friend]}")  
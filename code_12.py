# Dictionary Comprehension

users = [
    (0, "James", "password1"),
    (1, "Joe", "password2"),
    (2, "Greg", "password3"),
    (3, "Mike", "password4"),
]

username_mapping = { user[1]: user for user in users }

# print(username_mapping)

username_input = input("Enter your username:\n")

_, username, password = username_mapping[username_input]

print(f"User: {username}, Password: {password}")
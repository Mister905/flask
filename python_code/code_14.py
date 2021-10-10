# Unpacking keyword arguments

def print_keyword_args(**kwargs):
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")

details = { "name": "James", "age": 25 }

print_keyword_args(**details)
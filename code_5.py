list_example = [ "James", "Joe", "John" ]

# The important difference is that tuples are immutable
tuple_example = ( "James", "Joe", "John" )

# Sets cannot have two items with the same value. Unlike lists and tuples, sets do not maintain order
set_example = { "James", "Joe", "John" }

list_example.append("Jerry")

print(list_example[0])

print(tuple_example[2])

print(list_example[len(list_example) - 1])
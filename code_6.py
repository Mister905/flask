# Set operations

friends = { "Bob", "Rolf", "Anne" }

abroad = { "Bob", "Anne" }

# The function difference() returns a set that is the difference between two sets.
local_friends = friends.difference(abroad)

print(local_friends)

# Return a set that contains all items from both sets, duplicates are excluded
total_friends = friends.union(abroad)

print(total_friends)

# Return a set that contains the items that exist in both sets
both = friends.intersection(abroad)

print(both)
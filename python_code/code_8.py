# List Comprehension

numbers = [ 1, 3, 5 ]

doubled = [ number * 2 for number in numbers ]

for number in doubled:
    print(number)
    
friends = [ "Steve", "Sam", "Stu", "Chad" ]

starts_with_s = [ friend for friend in friends if friend.startswith("S") ]

print(starts_with_s)
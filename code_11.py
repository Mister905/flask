def divide(dividend, divisor):
    
    if divisor != 0:
        print(dividend / divisor)
    else:
        print("Divide by 0 error")
        
divide(dividend=12, divisor=4)


# Function with default parameters

def add(x, y=8):
    print(x+y)
    
add(x=5)


# Functions returning values

def return_sum(x,y):
    return x+y

my_sum = return_sum(5, 5)

print(my_sum)


# Lambda Functions

def double(x):
    return x * 2

sequence = [ 1, 3, 5, 9 ]

doubled = [double(x) for x in sequence]

print(doubled)
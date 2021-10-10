def multiply(*args):
    
    total = 1
    
    for arg in args:
        total = total * arg
        
    return total
    
    
product = multiply(1, 3, 5)

print(product)

def apply(*args, operator):
    if operator == "*":
        return multiply(*args)
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to apply."
    
print(apply(1, 3, 5, 7, operator="*"))
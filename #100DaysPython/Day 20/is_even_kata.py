def is_even(n): 
    
    # your code here
    if n < 0:
        n = -n
    
    if n == 0:
        return True
    elif n % 2 == 0:
        return True
    else:
        return False
        
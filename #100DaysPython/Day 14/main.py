def make_negative( number ):
    if number == 0:
        return number
    elif number == -number:
        return number
    else:
        return number
    
num = make_negative(-42)
print(num)
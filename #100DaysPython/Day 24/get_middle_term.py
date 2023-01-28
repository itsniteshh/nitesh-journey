def get_middle(s):
    """for getting middle term from a series"""
    mid_length = int((len(s) / 2) ) #gets the starting length of the mid character
    
    if len(s) % 2 == 0:
        return s[mid_length-1:mid_length+1]
    else:
        return s[mid_length]
    


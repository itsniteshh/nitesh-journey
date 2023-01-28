geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    """function to filter out the geese list elements if present in the array"""
    new_list = []
    
    for items in birds:
        if items in geese:
            pass
        else:
            new_list.append(items)
    return new_list


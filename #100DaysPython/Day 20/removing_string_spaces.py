def no_space(x):
    #a function to remove spaces without using strip functions
    new_str = ""
    for words in x:
        if words == " ":
            pass
        else:
            new_str += words
            
    return new_str


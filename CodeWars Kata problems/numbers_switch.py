def switch_it_up(number):
    #your code here
    numbers = {
        "1": "One",
        "2": "Two",
        "3": "Three",
        "4": "Four",
        "5": "Five",
        "6": "Six",
        "7": "Seven",
        "8": "Eight",
        "9": "Nine",
        "0": "Zero"
    }
    result = ""
    for num in str(number):
        result = numbers.get(num)
    
    return result
        
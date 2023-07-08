
def find_max(numbers):
    #to find the larges num in a list
    max = 0

    for num in numbers:
        if num > max:
            max = num

    return max
        
maxi = find_max([4, 5, 2, 434, 43, 32, 6543, 32])
print(maxi)
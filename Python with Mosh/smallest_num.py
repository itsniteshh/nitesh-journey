
numbers = [5, 19, 3, 0, 42, 13, 84, -1, 94]

#var to store the smallest num which alrady has first num from list
smallest_num = numbers[0]


for num in numbers:
    if num < smallest_num:
        smallest_num = num
        
print(f"The smallest number is {smallest_num}")
        
#to find the smallest num in the list

nums = [3, 6, 2, 8, 1, 4, 10, 5, 80, ]

smallest_num = 900

for num in nums:
    if num < smallest_num:
        smallest_num = num
        
print(f"The smallest number is {smallest_num}")
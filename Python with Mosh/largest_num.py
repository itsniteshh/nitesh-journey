#to find the largest num in the list

nums = [3, 6, 2, 8, 4, 10, 5, 80, 3]

largest_num = 0

for num in nums:
    if num > largest_num:
        largest_num = num
        
print(f"The largest number is {largest_num}")
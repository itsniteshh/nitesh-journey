numbers = [5, 19, 3, 42, 13, 84, -1, 94, 0]

#var to store the largest num from the list
largest_num = 0

for num in numbers:
    #checking if num from list is greated than largest num variable
    if num > largest_num:
        largest_num = num
  
        
print(f"The largest number is {largest_num}")
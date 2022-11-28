#removing dup from list
numbers = [2, 3, 7, 4, 2, 4, 7, 43, 1, 6]

new_num = []

for num in numbers:
    if num not in new_num:
        new_num.append(num)

print(new_num)
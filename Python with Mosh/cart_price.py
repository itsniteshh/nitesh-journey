#an app for calculating total prize of items in our cart

prices = [10, 40, 42, 539, 23]

total_price = 0

for nums in prices:
    total_price += nums
    
print(f"The total price of items in our cart is {total_price}")
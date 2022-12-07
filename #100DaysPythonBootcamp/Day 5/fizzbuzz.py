#Write your code below this row 👇
for nums in range(100):
    if nums % 15 == 0:
        print("FizzBuzz")
    elif nums % 3 == 0:
        print("Fizz")
    elif nums % 5 == 0:
        print("Buzz")
    else:
        print(nums)

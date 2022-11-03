# a dict to return nums in text based on input nums

num = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "0": "zero"
}



user_input = (input("Phone: "))
for n in user_input:
    print(num[user_input])

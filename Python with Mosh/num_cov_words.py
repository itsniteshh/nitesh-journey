numbers = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    0: "zero"
}


new_num = ""
user_input = input("Phone: ")

for nums in user_input:
    new_num += numbers.get(int(nums)) + " "
        
        
print(new_num)


telephone_dict = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "Seven",
    8: "eight",
    9: "nine",
    0: "zero"
}
word = ""

num =  input("Phone: " )
for n in num:
    word += telephone_dict.get(int(n)) + " "
    
    
    
print(word)
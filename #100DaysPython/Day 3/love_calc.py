# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

both_name = name1 + name2

result1= both_name.count("t") + both_name.count("r") + both_name.count("u") + both_name.count("e")

result2= both_name.count("l") + both_name.count("o") + both_name.count("v") + both_name.count("e")

print(f"Your total love score is {result1}{result2}")
# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
random_payer = random.randint(0, len(names)-1)
payer = names[random_payer]

print(f"{payer} is going to buy us the meal today!")
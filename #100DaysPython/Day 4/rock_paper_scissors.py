rock = '''
Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
Paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

games = [rock, paper, scissors]
#user guess
user_gues = int(input("Enter you guess: press 0 for rock, 1 for paper and 2 for scissors \n"))
user_guess = games[user_gues]
print(f"\nUser chose: {user_guess}")

#com guess
computer_guess = random.randint(0, len(games)- 1)
com_guess = games[computer_guess]
print(f"Com chose: {com_guess}")

#logic comparison 

if user_guess == com_guess:
  print("Match drawn")
elif user_guess == rock and com_guess == scissors:
  print("you win")
elif user_guess == scissors and com_guess == paper:
  print("you win")
elif user_guess == paper and com_guess == rock:
  print("you win")
else:
  print("you lose")





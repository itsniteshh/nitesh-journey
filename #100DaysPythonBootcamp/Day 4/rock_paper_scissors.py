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

#both party guesses
com_guess = random.randint(0, len(games) - 1)
user_guess = int(input("Enter your guess: 0 for rock, 1 for paper, 2 for scissors\n"))

com_final = games[com_guess]
user_final = games[user_guess]

print(f"Com chose {com_final}")
print(f"\nUser chose {user_final}")

#conditionals
if user_final == com_final:
    print("match drawn")
elif user_final == 0 and com_final == 2:
    print("You win")
elif user_final == 2 and com_final == 1:
    print("You win")
elif user_final == 1 and com_final == 0:
    print("You win")
elif user_final == 2 and com_final == 0:
    print("You Lose")
elif user_final == 1 and com_final == 2:
    print("You Lose")
elif user_final == 0 and com_final == 1:
    print("You Lose")
else:
    print("Invalid input")

from art import logo, vs
import random
from game_data import data
#from replit import clear
count = 0

def random_guesses(d):
  #function to randomly guess
  new_data = random.choice(data)
  return new_data

a = random_guesses(data)


def comparing_both(char1, char2):
  #function to compare within 2 datas
  forA = char1.get("follower_count")
  forB = char2.get("follower_count")

  if forA > forB:
    return True
  else:
    return False

#repeating random guess
while True:
  b = random_guesses(data)
  print(logo)
  if count > 0:
    print(f"You're right! Current score {count}")
    
  num1 = (f"Compare A: {a.get('name')}, a {a.get('description')}, from {a.get('country')}.")
  print(num1)
  #checking to see if the user guesses correctly
                                                                     
  num2 = (f"Compare B: {b.get('name')}, a {b.get('description')}, from {b.get('country')}.")
  print(vs)
  print(num2)
  user_input = input("Who has more followers 'A' or 'B': ").lower()
  
  #if correct guess, show score and make B into A
  is_logic_true = comparing_both(a, b)
  if is_logic_true:
    #clear()
    num1 = num2
    count += 1
  else:
    print("You lose")
    print(f"your final score is {count}")
    break
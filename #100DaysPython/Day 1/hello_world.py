#print("HEllo world")

import random 
#from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = random.choices(cards, k=2)
com_cards = random.choices(cards, k=2)


def user_calc(user_cards):
  pass
  

while True:
  #print(logo)
  another_try = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
  if another_try == 'n':
    break
  else:
    print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
    print(f"Computer's first card: {com_cards[0]}")
    
    



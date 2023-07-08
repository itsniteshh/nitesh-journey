import random

my_guess = 7

lives = 3

while lives > 0:
    print("Hey com, guess the secret number")
    com_guess = random.randint(1, 7)
    print(f"The com guessed {com_guess}")
    
    if com_guess == my_guess:
        break
    else:
        lives -= 1
        
        
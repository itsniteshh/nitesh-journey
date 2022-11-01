import random

random_guess = random.randint(0, 100)
print(random_guess)


guess_count = 0
total_guess = 3

while True:
    user_guess = int(input("Enter a number from 1 to 100: \n"))
    if user_guess == random_guess:
        print(f"You guessed the number {random_guess} correctly")
        break
    else:
        guess_count += 1
        
    
    if guess_count >= total_guess:
        print(f"Sorry you are out of guesses!")
        break
    
    
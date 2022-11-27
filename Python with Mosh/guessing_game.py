secret_num = 43

guess_count = 0
total_guess = 3


while True:
    user_guess = int(input("Enter your guess: \n"))
    #for counting the guesses and incrementing it by 1 for every wrong guess
    guess_count += 1
    
    if user_guess == secret_num:
        print(f"You guessed the number {secret_num} correctly! YOU WIN!")
        break
    elif user_guess > secret_num:
        print("Guess too high!")
    else:
        print("Guess too low!")
        
     
    #checking to see if user guess > total given guess
    if guess_count >= total_guess:
        print("You're out of guesses! YOU LOSE!!")
        break
    
        



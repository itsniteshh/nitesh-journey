secret_num = 9

guess_count = 3

while guess_count > 0:
    guess = int(input("Enter your guess: "))
    guess_count -= 1
    
    if guess == secret_num:
        print(f"You guessed the number {secret_num} correctly")
        break
    else:
        print("That was a wrong guess")
    
    
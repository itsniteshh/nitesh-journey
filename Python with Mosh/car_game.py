user_input = ""
started = False


while True:
    #Build a car game that prompts help manual when user types help 
    user_input = input("> ").lower()
    
    if user_input == "help":
        print("""
              Start - to start the car \nstop - to stop the car \nquit - to exit the game
              """.strip())
        
    elif user_input == "quit":
        break
    
    elif user_input == "start":
        if started:
            print("Car is already running")
        else:
            started = True
            print("Car started.... Ready to go")
    
    elif user_input == "stop":
        if not started:
            print("Car is already stopped")
        else:
            started = False
            print("Car is stopped")
                       
        
    else:
        print("Sorry, I don't understand your language!")
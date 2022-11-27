#a game which shows commands when typed help and so
is_started = False

while True:
    user_input = input("\n>").lower()
    
    if user_input == "quit":
        break
    
    elif user_input == "help":
        print("""
start- to start the car
stop - to stop the car
quit - to exit""")
        
    elif user_input == "start":
        if is_started:
            print("The car is already running....")
            
        else:
            is_started = True
            print("The car started")
    
    elif user_input == "stop":
        if not is_started:
            print("The car is already stopped")
        else:
            print("The car is stopped")
            is_started = False
    
    else:
        print("Wrong input!")
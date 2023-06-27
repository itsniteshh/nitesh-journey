
is_car_running = False
#is_car_stopped = True

while True:
    # loop to run a car 
    
    user = input()
    
    if user == "help":
        print('''
start - to start the car
stop - to stop the car
quit - to exit
              ''')
        
    if user == "quit":
        break
        
    elif user == "start":
        if is_car_running:
            print("The car is already running")
        else:
            is_car_running = True
            print("The car is running")
            
    elif user == "stop":
        if not is_car_running:
            print("The car is already stopped")
        else:
            is_car_running = False
            print("The car stopped")
            
            
    else:
        print("Wrong input")
            
            
            
            
    
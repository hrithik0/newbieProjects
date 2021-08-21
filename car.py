is_started = False
while True:
    user_input = input(">").strip().lower()
    if user_input == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to exit
        """)
    elif user_input == "start":
        if is_started:
            print("Car is already started!")
        else:
            is_started = True
            print("Car is started.")
    elif user_input == "stop":
        if not is_started:
            print("Car is already stopped!")
        else:
            print("Car is stopped.")
            is_started = False
    elif user_input == "quit":
        break
    else:
        print("I don't understand that..")

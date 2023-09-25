while True:
# Body of the loop
    user_input = input("Enter 'q' to quit: ")
# Check the condition to break out of the loop
    if user_input == 'q':
        break
    

try:
    while True:
        pass # Infinite loop
except KeyboardInterrupt:
    print("Program was interrupted by the user.")
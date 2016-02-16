# Continue And Break Statements

# Import the random module.
import random

# In this while loop, if the number is less than 3, the loop restarts again.
# If the number is 4, it changes running to false and the loop ends.
# If the number is 5, it breaks out of the loop and the loop ends.

# Set running to true
running = True

# while running is true
while running:
    # Create a random integer between 0 and 5
    s = random.randint(0,5)
    # If the integer is less than 3
    if s < 3:
        # Print this
        print('It is too small, starting over.')
        # Reset the next interation of the loop
        # (i.e skip everything below and restart from the top)
        continue
    # If the integer is 4
    if s == 4:
        running = False
        # Print this
        print('It is 4! Changing running to false')
    # If the integer is 5,
    if s == 5:
        # Print this
        print('It is 5! Breaking Loop!')
        # then stop the loop
        break









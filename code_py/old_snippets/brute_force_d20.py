# Brute Force D20 Roll Simulator

# Import random module
import random

# Create a variable with a TRUE value
rolling = True

# while rolling is true
while rolling:
    # create x, a random number between 0 and 99
    x = random.randint(0, 99)
    # create y, a random number between 0 and 99
    y = random.randint(0, 99)
    # if x is less than 2 and y is between 0 and 10
    if x < 2 and 0 < y < 10:
        # Print the outcome
        print('You rolled a {0}{1}.'.format(x, y))
        # And set roll of False
        rolling = False
    # Otherwise
    else:
        # Try again
        print('Trying again.')

# while Statement

# Based on: A Byte of Python

# While loops until a condition is true.


# Import the random module.
import random

# Create a variable of the true number of deaths of an event.
deaths = 6

# Create a variable that is denotes if the while loop for keep running.
running = True

# while running is True
while running:
    # Create a variable that randomly create a integer between 0 and 10.
    guess = random.randint(0,10)

    # if guess equals deaths,
    if guess == deaths:
        # then print this
        print('Correct!')
        # and then also change running to False to stop the script
        running = False
    # else if guess is lower than deaths
    elif guess < deaths:
        # then print this
        print('No, it is higher.')
    # if guess is none of the above
    else:
        # print this
        print('No, it is lower')

# By the output, you can see that the while script keeping generating guesses
# and checking them until guess matches deaths, in which case the script stops.


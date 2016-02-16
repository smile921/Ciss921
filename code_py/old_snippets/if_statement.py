# if Statement
# Based on: A Byte of Python

# Import the random module.
import random

# Create a variable of the true number of deaths of an event.
deaths = 6

# Create a variable that randomly create a integer between 0 and 10.
guess = random.randint(0,10)

# if guess equals deaths,
if guess == deaths:
    # then print this
    print('Correct!')
# else if guess is lower than deaths
elif guess < deaths:
    # then print this
    print('No, it is higher.')
# if guess is none of the above
else:
    # print this
    print('No, it is lower')

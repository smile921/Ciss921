#  File:       04-12.py 
#  Purpose:    The if statement with multiple statements
#  Programmer: Anne Dawson
#  Course:     CSCI120A, CSCI165
#  Date:       Monday 27th September 2004, 13:23 PT

#  The condition of the following if statement
#  follows the word if, and ends with a colon (:)
#  In this example, if x has a value equal to 'spammy',
#  then 'Hi spam\n' will be printed followed by
#  "Nice weather we're having"
#  followed by 'Have a nice day!'

x = 'spam'
if x == 'spammy':
    print ('Hi spam\n')
    print ("Nice weather we're having")
    print ('Have a nice day!')
else:
    print ('not spam')
    print ('Not having a good day?')

# Notice the indentation (spacing out) of this code.
# The statement(s) following the if condition (i.e. boolean expression)
# must be indented to the next tab stop. This means you must press
# the Tab button before typing the word print.
# Try removing the tab spaces and see what happens when you attempt to run.

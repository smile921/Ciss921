# String Formatting

# Print a string with 1 digit and one string.
print('This is %d %s bird!' % (1, 'dead'))

# Print a dictionary based string
print('%(number)d more %(food)s' % {'number' : 1, 'food' : 'burger'})

# Import the sys module
import sys

# Print a string about my laptop.
print('My {1[kind]} runs {0.platform}'.format(sys, {'kind': 'laptop'}))

# String Formatting Codes
# %s string
# %r repr string
# %c character (integer or string)
# %d decimal
# %i integer
# %x hex integer
# %X same as X but with uppercase
# %e floating point lowercase
# %E floating point uppercase
# %f floating point decimal lowercase
# %F floating point decimal uppercase
# %g floating point e or f
# %G floating point E or F
# %% literal %

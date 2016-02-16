# Import the regex (re) package
import re

########

# Import sys

# Create a simple text string.
text = "{'addressComponents': {'formattedAddress': 'Sundar Bajar, Lamjung'}, 'coords': [84.42, 28.132838]}"

# Create a pattern to match
three_letter_word = '\d{3}.\d{4}'

# Convert the string into a regex object
pattern_re = re.compile(three_letter_word)

# re.search

# Does a three letter word appear in text?
re_search = re.search('\d{2}.\d{2}, \d{2}.\d{2}', text)

# If the search query is at all true,
if re_search:
    # Print the search results
    print(re_search.group())

# Regular Expressions
# Based on: http://www.tutorialspoint.com/python/python_reg_expressions.htm

# Import the regex (re) package
import re

# Import sys

# Create a simple text string.
text = 'The quick brown fox jumped over the lazy black bear.'

# Create a pattern to match
three_letter_word = '...'

# Convert the string into a regex object
pattern_re = re.compile(three_letter_word); print(pattern_re)

# re.search

# Does a three letter word appear in text?
re_search = re.search('..own', text)

# If the search query is at all true,
if re_search:
    # Print the search results
    print(re_search.group())

# re.match

# re.match() is for matching ONLY the beginning of a string or the whole string
# For anything else, use re.search

# Match all three letter words in text
re_match = re.match('..own', text)

# If re_match is true,
if re_match:
    # Print all the matches
    print(re_match.group())
else:
    # Print this
    print('No matches')

# re.split

# Split up the string using "e" as the seperator.
re_split = re.split('e', text); print(re_split)

# re.sub: Replaces occurrences of the regex pattern with something else
# The "3" references to the maximum number of substitutions to make.

# Substitute the first three instances of "e" with "E", then print it
re_sub = re.sub('e', 'E', text, 3); print(re_sub)

# Patterns

# ^   Matches beginning of line.
# $   Matches end of line.
# .   Matches any single character except newline.
# [...]   Matches any single character in brackets.
[# ^...]  Matches any single character not in brackets
# re* Matches 0 or more occurrences of preceding expression.
# re+ Matches 1 or more occurrence of preceding expression.
# re? Matches 0 or 1 occurrence of preceding expression.
# re{ n}  Matches exactly n number of occurrences of preceding expression.
# re{ n,} Matches n or more occurrences of preceding expression.
# re{ n, m}   Matches at least n and at most m occurrences of preceding expression.
# a | b    Matches either a or b.
# (re)    Groups regular expressions and remembers matched text.
# (?imx)  Temporarily toggles on i, m, or x options within a regular expression. If in parentheses, only that area is affected.
# (?-imx) Temporarily toggles off i, m, or x options within a regular expression. If in parentheses, only that area is affected.
# (?: re) Groups regular expressions without remembering matched text.
# (?imx: re)  Temporarily toggles on i, m, or x options within parentheses.
# (?-imx: re) Temporarily toggles off i, m, or x options within parentheses.
# (?#...) Comment.
# (?= re) Specifies position using a pattern. Doesn't have a range.
# (?! re) Specifies position using pattern negation. Doesn't have a range.
# (?> re) Matches independent pattern without backtracking.
# \w  Matches word characters.
# \W  Matches nonword characters.
# \s  Matches whitespace. Equivalent to [\t\n\r\f].
# \S  Matches nonwhitespace.
# \d  Matches digits. Equivalent to [0-9].
# \D  Matches nondigits.
# \A  Matches beginning of string.
# \Z  Matches end of string. If a newline exists, it matches just before newline.
# \z  Matches end of string.
# \G  Matches point where last match finished.
# \b  Matches word boundaries when outside brackets. Matches backspace (0x08) when inside brackets.
# \B  Matches nonword boundaries.
# \n, \t, etc.    Matches newlines, carriage returns, tabs, etc.
# \1...\9 Matches nth grouped subexpression.
# \10 Matches nth grouped subexpression if it matched already. Otherwise refers to the octal representation of a character code.

# Examples

# [Pp]ython   Match "Python" or "python"
# rub[ye] Match "ruby" or "rube"
# [aeiou] Match any one lowercase vowel
# [0-9]   Match any digit; same as [0123456789]
# [a-z]   Match any lowercase ASCII letter
# [A-Z]   Match any uppercase ASCII letter
# [a-zA-Z0-9] Match any of the above
# [^aeiou]    Match anything other than a lowercase vowel
# [^0-9]  Match anything other than a digit

# ruby?   Match "rub" or "ruby": the y is optional
# ruby*   Match "rub" plus 0 or more ys
# ruby+   Match "rub" plus 1 or more ys
# \d{3}   Match exactly 3 digits
# \d{3,}  Match 3 or more digits
# \d{3,5} Match 3, 4, or 5 digits

# ^Python Match "Python" at the start of a string or internal line
# Python$     Match "Python" at the end of a string or line
# \APython    Match "Python" at the start of a string
# Python\Z    Match "Python" at the end of a string
# \bPython\b  Match "Python" at a word boundary
# \brub\B \B is nonword boundary: match "rub" in "rube" and "ruby" but not alone
# Python(?=!) Match "Python", if followed by an exclamation point
# Python(?!!) Match "Python", if not followed by an exclamation point

# python|perl Match "python" or "perl"
# rub(y|le))  Match "ruby" or "ruble"
# Python(!+|\?)   "Python" followed by one or more ! or one ?

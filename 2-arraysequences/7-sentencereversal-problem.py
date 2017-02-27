# Sentence Reversal

"""
Problem:

Given a string of words, reverse all the words. For example:

Given:
'This is the best'

Return:
'best the is This'

As part of this exercise you should remove all leading and trailing whitespace.
So that inputs such as:
'  space here'  and 'space here      '

both become:
'here space'
"""

# Solution 1

"""
We could take advantage of Python's abilities and solve the problem with the use
 of split() and some slicing or use of reversed:
"""

def rev_word1(s):
    return " ".join(reversed(s.split()))

#OR

def rev_word2(s):
    return " ".join(s.split()[::-1])

"""
While both of those solutions are valid a more manual approach would be to loop
over the text and extract words form the string ourselves.
Then we can push the words to a "stack" and in the end opo them all to reverse.
"""

def rev_word3(s):
    words = []
    length = len(s)
    spaces = [' ']

    # Index tracker
    i = 0

    # While we haven't iterated through the entire string
    while i < length:

        # if current letter is not a space then we know a word starts at that index
        if s[i] not in spaces:

            # we know a word starts at that index
            word_start = i

            # keep going until we haven't hit another space
            while i < length and s[i] not in spaces:

                # get index where word ends
                i += 1
            # append that word to the list
            words.append(s[word_start:i])
        # add to index
        i += 1

    # join the reversed words
    return " ".join(reversed(words))

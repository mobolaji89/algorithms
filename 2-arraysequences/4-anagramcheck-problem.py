#Anagram Check

"""
Problem:

Given two strings, check to see if they are anagrams.
An anagram is when the two strings can be written using the exact same letters
(so you can just rearrange the letters to get a different phrase or word).

For example:

"public relations" is an anagram of "crap built on lies"

"clint eastwood" is an anagram of "old west action"

Note: Ignore spaces and capitalization.
So "d go" is an anagram of "God" and "dog" and "o d g".
"""

# My Initial Solution
def anagram(s1,s2):

    s1 = s1.lower().replace(" ","")
    s2 = s2.lower().replace(" ","")

    s1 = sorted(s1)
    s2 = sorted(s2)

    if s1 == s2:
        print(True)
    else:
        print(False)

anagram("Do g", "god")
anagram("public relations", "crap built on lies")
anagram("clint eastwood", "old west action")

# First Solution
def anagram(s1, s2):

    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()

    return sorted(s1) == sorted(s2)

# Alternate (more optimal) Solution
def anagram2(s1,s2):

    # Remove spaces and lowercase letters
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()

    # Edge Case to check if same number of letters
    if len(s1) != len(s2):
        return False

    # Create counting dictionary
    count = {}

    # Fill dictionary for first string (add counts)
    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    # Fill dictionary for second string (subtract counts)
    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    # Check that all counts are 0
    for k in count:
        if count[k] != 0:
            return False

    # Otherwise they're anagrams
    return True

"""
Note for the second solution: The use of DefaultDict from the Collections
module would clean up this code quite a bit, and the final for loop could be built
into the second for loop, but in the above implementation every step is very clear.
"""

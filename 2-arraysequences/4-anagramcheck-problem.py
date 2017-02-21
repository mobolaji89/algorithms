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

# My Inital Solution

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

# Recommended Solution
def anagram(s1, s2):

    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()

    return sorted(s1) == sorted(s2)

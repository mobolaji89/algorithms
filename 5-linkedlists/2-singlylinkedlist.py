class Node(object):

    def __init__(self, value):

        self.value = value
        self.next = None


# Pros
"""
Linked Lists have constant-time insertions and deletions in any position,
in comparison, arrays require O(n) time to do the same thing.

Linked lists can continue to expand without having to specify their size ahead
of time.
"""

# Cons
"""
To access an element in a linked list, you need to take O(k) time to go from the
head of the list to the kth element. In contrast, arrays have constant
time operations to access elements in an array.
"""

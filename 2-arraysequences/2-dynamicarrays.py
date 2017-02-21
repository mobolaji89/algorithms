# Dynamic Arrays

"""
When you're create a list in Python, you don't need to specify how large an
array is beforehand.

A list instance often has greater capacity than it's current length.
For example, if you have a list with 3 elements in it, usually that list
is going to have a greater capacity to hold more elements than just the 3
you initiated.
If elements keep getting appended, eventually this extra space runs out.
"""

# Example

import sys

n = 10

data = []

for i in range(n):

  # Number of elements
  a = len(data)

  # Actual Size in Bytes
  b = sys.getsizeof(data)

  print('Length: {0:3d}; Size in bytes: {1:4d} '.format(a, b))

  #increase length by one
  data.append(n)
  """
  Length:   0; Size in bytes:   64
  Length:   1; Size in bytes:   96
  Length:   2; Size in bytes:   96
  Length:   3; Size in bytes:   96
  Length:   4; Size in bytes:   96
  Length:   5; Size in bytes:  128
  Length:   6; Size in bytes:  128
  Length:   7; Size in bytes:  128
  Length:   8; Size in bytes:  128
  Length:   9; Size in bytes:  192
  """

"""
What Python has done, is it's actually set a number of bytes larger than
what it needs to hold the current elements in the list, while it's appending
new elements appending new elements to the array.
"""
